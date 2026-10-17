"""Small packaged server-side part of the reviewed German UI dictionary."""

import json
from functools import cache
from importlib.resources import files
from typing import Any, cast


@cache
def _texts() -> dict[str, str]:
    return cast(
        dict[str, str],
        json.loads(
            files("core_contracts").joinpath("resources/de.json").read_text(encoding="utf-8")
        ),
    )


def user_text(key: str, *, fallback: str | None = None, **values: Any) -> str:
    texts = _texts()
    text = texts.get(key, texts.get(fallback or "", key))
    for name, value in values.items():
        text = text.replace("{" + name + "}", str(value))
    return text
