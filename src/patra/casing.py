"""Title-casing with Indian place-name exceptions."""

# Words that should stay lowercase (articles, prepositions in place names)
_LOWER_WORDS = frozenset(["and", "of", "the", "in", "at", "by"])

# Words that should stay uppercase (common abbreviations in addresses)
_UPPER_WORDS = frozenset(["ngo", "co", "pvt", "ltd", "llp"])


def title_case(s: str) -> str:
    """Title-case a string with exceptions for common Indian address words."""
    words = s.split(" ")
    result: list[str] = []
    for i, word in enumerate(words):
        lower = word.lower()
        upper = word.upper()
        if upper in _UPPER_WORDS:
            result.append(upper)
        elif i > 0 and lower in _LOWER_WORDS:
            result.append(lower)
        else:
            result.append(word.capitalize())
    return " ".join(result)
