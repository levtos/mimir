"""Repeat the source-checked pipeline twice; compare every output hash."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REVISION = "70b6e83b26a930632c7b2430fb6d5b955ec63158"


def main():
    source = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as folder:
        command = [
            sys.executable,
            str(ROOT / "dev/build_herd_assets.py"),
            "--source",
            str(source),
            "--source-revision",
            SOURCE_REVISION,
            "--output",
            folder,
        ]
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        manifest = ROOT / "docs/alpha10/herde-ableitungen.json"
        first = manifest.read_bytes()
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        if first != manifest.read_bytes():
            raise SystemExit("Herd pipeline is not reproducible")
        print(json.dumps({"identical_hashes": True, "source_revision": SOURCE_REVISION}))


if __name__ == "__main__":
    main()
