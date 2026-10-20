"""Finite text operations; pattern matching uses bounded shell globs, never regex code."""

import json
from datetime import datetime
from fnmatch import fnmatchcase

from .declarative_models import TextRule
from .quality import FieldValue, ReasonCode, derive, unknown


def normalize_key(value: str, delimiters: str = "_- ", separator: str = " ") -> str:
    """Pinned, finite normalization shared by rules, catalogs and import planning."""
    translation = str.maketrans({char: " " for char in delimiters})
    return separator.join(value.lower().translate(translation).split())


def evaluate_text(rule: TextRule, args: list[FieldValue], now: datetime) -> FieldValue:
    if any(not arg.usable(now) for arg in args):
        return derive(None, args, now)
    strings = [arg.value for arg in args]
    if any(not isinstance(value, str) or len(value) > 8192 for value in strings):
        return unknown(ReasonCode.INVALID_VALUE, rule.op, now)
    match rule.op:
        case "lower":
            result = strings[0].lower()
        case "strip":
            result = strings[0].strip()
        case "normalize_key":
            result = normalize_key(strings[0], rule.delimiters, rule.separator)
        case "contains":
            result = strings[1] in strings[0]
        case "matches":
            if len(strings[1]) > 256:
                return unknown(ReasonCode.INVALID_VALUE, "pattern", now)
            result = fnmatchcase(strings[0], strings[1])
        case "compound_key":
            result = json.dumps(strings, ensure_ascii=False, separators=(",", ":"))
    return derive(result, args, now)
