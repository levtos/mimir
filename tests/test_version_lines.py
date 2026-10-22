import subprocess
from pathlib import Path

import pytest
import yaml

from dev.version_gate import bridge_version_errors, compare_tags


@pytest.fixture
def tagged_repo(tmp_path):
    def run(*args):
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)

    run("init")
    run("config", "user.name", "Version test")
    run("config", "user.email", "version@example.invalid")

    def tag(name, slug):
        path = tmp_path / "an-arbitrary-directory/config.yaml"
        path.parent.mkdir(exist_ok=True)
        path.write_text(yaml.safe_dump({"slug": slug, "version": name.removeprefix("v")}))
        run("add", ".")
        run("commit", "-m", name)
        run("tag", name)

    return tmp_path, tag


def test_slug_is_read_from_each_tag_and_not_its_directory(tagged_repo):
    root, tag = tagged_repo
    tag("v1.0.0a7.post1", "core_contracts")
    tag("v1.0.0a7", "mimir")
    report = compare_tags(root, "1.0.0a8", "mimir", ["v1.0.0a7.post1", "v1.0.0a7"])
    assert report["passed"]
    other = next(row for row in report["comparisons"] if row["tag"].endswith("post1"))
    assert other["classification"] == "andere App" and not other["newer"]
    (root / "an-arbitrary-directory/config.yaml").write_text("slug: unrelated\n")
    assert compare_tags(root, "1.0.0a8", "mimir", ["v1.0.0a7.post1"])["passed"]


def test_wrong_same_slug_and_any_older_tag_block(tagged_repo):
    root, tag = tagged_repo
    tag("v1.0.0a7.post1", "mimir")
    tag("v1.0.0a6", "mimir")
    assert not compare_tags(root, "1.0.0a8", "mimir", ["v1.0.0a7.post1", "v1.0.0a6"])["passed"]


def test_missing_metadata_and_suffix_fail(tagged_repo):
    root, tag = tagged_repo
    tag("v1.0.0a1", "mimir")
    for candidate in ("1.0.0a8.post1", "1.0.0a8.dev1", "1.0.0a1"):
        assert not compare_tags(root, candidate, "mimir", ["v1.0.0a1"])["passed"]
    assert not compare_tags(root, "1.0.0a8", "mimir", [])["passed"]
    assert not compare_tags(root, "1.0.0a8", "mimir", ["v9.0.0"])["passed"]


@pytest.mark.parametrize("mode", ["ci", "release"])
@pytest.mark.parametrize("candidate", ["1.0.0a8", "1.0.0a10", "1.0.0a11"])
def test_ci_allows_equality_but_release_requires_newer(tagged_repo, mode, candidate):
    root, tag = tagged_repo
    tag("v1.0.0a9", "wuschel")
    tag("v1.0.0a10", "wuschel")
    tag("v9.0.0", "other_app")
    report = compare_tags(
        root, candidate, "wuschel", ["v1.0.0a9", "v1.0.0a10", "v9.0.0"], mode=mode
    )
    expected = candidate == "1.0.0a11" or (candidate == "1.0.0a10" and mode == "ci")
    assert report["passed"] is expected
    assert report["mode"] == mode
    assert len(report["comparisons"]) == 3


def test_terra_app_store_entry_is_unchanged():
    root = Path(__file__).resolve().parents[1]
    original = subprocess.check_output(
        ["git", "-C", str(root), "show", "a08a51d:core_contracts/config.yaml"]
    )
    assert (root / "core_contracts/config.yaml").read_bytes() == original
    mimir = yaml.safe_load((root / "wuschel/config.yaml").read_text(encoding="utf-8"))
    assert mimir["slug"] == "wuschel" and mimir["name"] == "Wuschel"
    assert mimir["image"] == "ghcr.io/levtos/{arch}-wuschel"


def test_independent_bridge_version_requires_unchanged_tagged_code(tagged_repo):
    root, tag = tagged_repo
    bridge = root / "custom_components/traber"
    bridge.mkdir(parents=True)
    source = bridge / "__init__.py"
    source.write_text("# released bridge\n")
    tag("v1.0.0b1", "wuschel")
    assert not bridge_version_errors(root, "1.0.0b2", "1.0.0b1")
    source.write_text("# modified bridge\n")
    assert bridge_version_errors(root, "1.0.0b2", "1.0.0b1")
    assert not bridge_version_errors(root, "1.0.0b2", "1.0.0b2")
    assert bridge_version_errors(root, "1.0.0b2", "1.0.0b3")
    assert bridge_version_errors(root, "1.0.0b2", "1.0.0a10")
