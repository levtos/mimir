import json
from pathlib import Path

import numpy as np
from PIL import Image

from dev.build_herd_assets import resize_premultiplied

ROOT = Path(__file__).resolve().parents[1]


def test_invisible_rgb_cannot_bleed_into_visible_edges():
    first = np.zeros((8, 8, 4), dtype=np.uint8)
    first[:, :, :3] = (255, 0, 255)
    first[2:6, 2:6] = (15, 92, 102, 255)
    second = first.copy()
    second[first[:, :, 3] == 0, :3] = (0, 255, 0)
    assert (
        resize_premultiplied(Image.fromarray(first), (4, 4)).tobytes()
        == resize_premultiplied(Image.fromarray(second), (4, 4)).tobytes()
    )


def test_manifest_budgets_dimensions_alpha_and_no_originals_in_bundle():
    manifest = json.loads(
        (ROOT / "docs/alpha10/herde-ableitungen.json").read_text(encoding="utf-8")
    )
    figures = [(name, item) for name, item in manifest["files"].items() if name.endswith(".webp")]
    assert len(figures) == 18
    for name, item in figures:
        assert item["size"] in ([512, 768], [1024, 1536])
        assert item["bytes"] <= (150000 if item["size"][0] == 512 else 400000)
        assert item["lossless_alpha_verified"] is True
    public = list((ROOT / "frontend/public/herde").glob("*"))
    assert all(path.name.startswith(("wuschel-", "traber-")) for path in public)
    assert not any(path.name.endswith("-figur.png") for path in public)
