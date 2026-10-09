"""Whitespace normalisation: collapse runs, strip leading/trailing."""
import re

_WHITESPACE_RE = re.compile(r"\s+")


def normalise_whitespace(s: str) -> str:
    """Collapse all whitespace runs to a single space and strip ends."""
    return _WHITESPACE_RE.sub(" ", s).strip()
