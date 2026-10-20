"""Reproducible approved-source pipeline; never modifies an original."""

import argparse
import hashlib
import io
import json
import shutil
from pathlib import Path

import numpy as np
import PIL
from PIL import Image, ImageDraw, features

PILLOW_VERSION = "12.1.1"
NUMPY_VERSION = "2.4.2"
WEBP_VERSION = "1.6.0"
PETROL = (15, 92, 102)
NAMES = (
    "wuschel",
    "traber",
    "schnueffel",
    "kuschel",
    "funkel",
    "blinzel",
    "schlummer",
    "traeller",
    "pfoertchen",
)
SEAL_CROP = (420, 355, 840, 775)


def resize_premultiplied(
    image: Image.Image, size: tuple[int, int], invisible: tuple[int, int, int] = (0, 0, 0)
) -> Image.Image:
    """Filter linear-light RGB * alpha; hidden source RGB cannot bleed into edges."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.float64) / 255
    rgb, alpha = rgba[:, :, :3], rgba[:, :, 3]
    linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)

    def scale(values: np.ndarray) -> np.ndarray:
        return np.asarray(
            Image.fromarray(values.astype(np.float32)).resize(size, Image.Resampling.LANCZOS),
            dtype=np.float64,
        )

    a = np.clip(scale(alpha), 0, 1)
    premultiplied = np.stack(
        [scale(linear[:, :, channel] * alpha) for channel in range(3)], axis=-1
    )
    premultiplied = np.clip(premultiplied, 0, a[:, :, None])
    straight = np.divide(
        premultiplied, a[:, :, None], out=np.zeros_like(premultiplied), where=a[:, :, None] > 1e-8
    )
    srgb = np.where(straight <= 0.0031308, straight * 12.92, 1.055 * straight ** (1 / 2.4) - 0.055)
    pixels = np.rint(np.clip(np.dstack((srgb, a)), 0, 1) * 255).astype(np.uint8)
    pixels[pixels[:, :, 3] == 0, :3] = invisible
    return Image.fromarray(pixels, "RGBA")


def figure_canvas(image: Image.Image) -> tuple[Image.Image, dict]:
    crop = image.getchannel("A").getbbox()
    if crop is None:
        raise ValueError("empty_figure")
    cut = image.crop(crop)
    visible = image.getchannel("A").point(lambda alpha: 255 if alpha >= 8 else 0).getbbox()
    if visible is None:
        raise ValueError("missing_hoof_anchor")
    anchor = visible[3] - crop[1]
    trailing = cut.height - anchor
    # Preserve even alpha 1..7 outside the visible hoof. Its trailing pixels
    # may use the transparent bottom margin; no source content is discarded.
    scale = min(928 / cut.width, 1440 / anchor, 47 / trailing if trailing else 100)
    size = (round(cut.width * scale), round(cut.height * scale))
    cut = resize_premultiplied(cut, size)
    xy = ((1024 - size[0]) // 2, 1488 - round(anchor * scale))
    canvas = Image.new("RGBA", (1024, 1536))
    canvas.paste(cut, xy)
    return canvas, {
        "crop": list(crop),
        "source_hoof_anchor_y": visible[3] - 1,
        "hoof_anchor_alpha_threshold": 8,
        "trailing_low_alpha_pixels": trailing,
        "bottom_margin_exception": "Alpha 1..7 retained below visible hoof" if trailing else None,
        "canvas": [1024, 1536],
        "placement": list(xy),
        "baseline_exclusive": 1488,
        "minimum_margin": 48,
    }


def save_webp(image: Image.Image, target: Path, budget: int) -> dict:
    for quality in (82, 78, 74, 70, 66, 62, 58):
        stream = io.BytesIO()
        image.save(
            stream, "WEBP", lossless=False, quality=quality, alpha_quality=100, method=6, exact=True
        )
        data = stream.getvalue()
        if len(data) <= budget:
            restored = Image.open(io.BytesIO(data)).convert("RGBA")
            if restored.getchannel("A").tobytes() != image.getchannel("A").tobytes():
                raise ValueError("webp_alpha_must_be_lossless")
            target.write_bytes(data)
            return {
                "quality": quality,
                "method": 6,
                "alpha_quality": 100,
                "lossless_alpha_verified": True,
                "lossless_rgb": False,
                "exact": True,
                "budget_bytes": budget,
            }
    raise ValueError("figure_budget_exceeded")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    parser.add_argument("--source-revision")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tool-info", action="store_true")
    args = parser.parse_args()
    versions = {
        "pillow": PIL.__version__,
        "numpy": np.__version__,
        "libwebp": features.version("webp"),
    }
    if args.tool_info:
        print(json.dumps(versions))
        return
    if versions != {"pillow": PILLOW_VERSION, "numpy": NUMPY_VERSION, "libwebp": WEBP_VERSION}:
        raise SystemExit("Pinned image runtime required: " + json.dumps(versions))
    if not args.source or not args.output or not args.source_revision:
        parser.error("source, source-revision and output required")
    source, output = args.source.resolve(), args.output.resolve()
    repo = Path(__file__).resolve().parents[1]
    if source == output or source in output.parents:
        raise ValueError("source_must_not_be_output")
    expected = json.loads((repo / "docs/alpha10/herde-quellen.json").read_text(encoding="utf-8"))
    for item in expected:
        data = (source / item["name"]).read_bytes()
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError("source_hash_mismatch")
        image = Image.open(io.BytesIO(data))
        if list(image.size) != item["size"] or image.mode != "RGBA":
            raise ValueError("source_dimensions_mismatch")
    output.mkdir(parents=True, exist_ok=True)
    manifest = {
        "source_repository": "Levtos/control",
        "source_revision": args.source_revision,
        "tools": versions,
        "filter": "linear RGB, premultiplied alpha, Lanczos",
        "figures": {},
        "files": {},
    }

    def record(path: Path, settings: dict | None = None):
        image = Image.open(path)
        manifest["files"][path.name] = {
            "size": list(image.size),
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            **(settings or {}),
        }

    for name in NAMES:
        image = Image.open(source / f"{name}-figur.png").convert("RGBA")
        canvas, placement = figure_canvas(image)
        manifest["figures"][name] = placement
        for width, budget in ((512, 150_000), (1024, 400_000)):
            target = output / f"{name}-figur-{width}.webp"
            resized = resize_premultiplied(canvas, (width, width * 3 // 2))
            settings = save_webp(resized, target, budget)
            record(target, settings)
        icon = Image.open(source / f"{name}-icon.png").convert("RGBA")
        for size in (16, 32, 64, 128, 180, 256, 512):
            cropped = icon.crop(SEAL_CROP) if name == "wuschel" and size == 16 else icon
            derived = resize_premultiplied(cropped, (size, size), PETROL)
            if size == 180:
                background = Image.new("RGBA", derived.size, (*PETROL, 255))
                background.alpha_composite(derived)
                derived = background
            path = output / f"{name}-icon-{size}.png"
            derived.save(path, "PNG", optimize=False, compress_level=9)
            record(
                path,
                {
                    "lossless": True,
                    **(
                        {"source_crop": list(SEAL_CROP)} if name == "wuschel" and size == 16 else {}
                    ),
                },
            )
        for scale in (1, 2):
            logo = Image.new("RGBA", (250 * scale, 100 * scale))
            logo.paste(
                resize_premultiplied(icon, (100 * scale, 100 * scale), PETROL), (75 * scale, 0)
            )
            path = output / f"{name}-logo-{scale}.png"
            logo.save(path, "PNG", compress_level=9)
            record(path, {"lossless": True})
        print("Derived " + name + "; source unchanged", flush=True)
    public = repo / "frontend/public/herde"
    public.mkdir(parents=True, exist_ok=True)
    for name in ("wuschel", "traber"):
        for width in (512, 1024):
            shutil.copyfile(
                output / f"{name}-figur-{width}.webp", public / f"{name}-figur-{width}.webp"
            )
        for size in (32, 64):
            shutil.copyfile(output / f"{name}-icon-{size}.png", public / f"{name}-icon-{size}.png")
    shutil.copyfile(output / "wuschel-icon-128.png", repo / "wuschel/icon.png")
    shutil.copyfile(output / "wuschel-logo-1.png", repo / "wuschel/logo.png")
    for size in (16, 32, 180):
        shutil.copyfile(
            output / f"wuschel-icon-{size}.png", repo / f"frontend/public/favicon-{size}.png"
        )
    brand = repo / "custom_components/traber/brand"
    brand.mkdir(exist_ok=True)
    for filename, original in {
        "icon.png": "traber-icon-256.png",
        "icon@2x.png": "traber-icon-512.png",
        "logo.png": "traber-logo-1.png",
        "logo@2x.png": "traber-logo-2.png",
    }.items():
        shutil.copyfile(output / original, brand / filename)
    contact = Image.new("RGB", (900, 460), "#f3f4f6")
    draw = ImageDraw.Draw(contact)
    for row, background in enumerate(("#f3f4f6", "#101820")):
        draw.rectangle((0, row * 230, 900, (row + 1) * 230), fill=background)
        foreground = "#182630" if row == 0 else "#e7edf4"
        for col, name in enumerate(("wuschel", "traber")):
            x = col * 450
            draw.text((x + 16, row * 230 + 14), name, fill=foreground, font_size=20)
            for offset, size in zip((32, 120, 250), (16, 32, 128), strict=True):
                icon = Image.open(output / f"{name}-icon-{size}.png")
                contact.paste(icon, (x + offset, row * 230 + 70), icon)
                draw.text((x + offset, row * 230 + 45), str(size), fill=foreground, font_size=16)
    contact.save(repo / "docs/alpha10/icon-kontaktbogen.png")
    (repo / "docs/alpha10/herde-ableitungen.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "tools": versions,
                "figures": {
                    name: {
                        str(size): manifest["files"][f"{name}-figur-{size}.webp"]["bytes"]
                        for size in (512, 1024)
                    }
                    for name in NAMES
                },
                "originals_modified": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
