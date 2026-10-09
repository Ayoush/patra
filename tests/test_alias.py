"""Tests for state alias resolution."""
from patra.alias import resolve_state_alias


def test_or_resolves_to_odisha():
    assert resolve_state_alias("OR") == "Odisha"


def test_uk_resolves_to_uttarakhand():
    assert resolve_state_alias("UK") == "Uttarakhand"


def test_bombay_resolves_to_maharashtra():
    assert resolve_state_alias("Bombay") == "Maharashtra"


def test_orissa_resolves_to_odisha():
    assert resolve_state_alias("Orissa") == "Odisha"


def test_pondicherry_resolves_to_puducherry():
    assert resolve_state_alias("Pondicherry") == "Puducherry"


def test_canonical_name_unchanged():
    assert resolve_state_alias("Maharashtra") == "Maharashtra"


def test_unknown_name_unchanged():
    assert resolve_state_alias("Neverland") == "Neverland"


def test_case_insensitive():
    assert resolve_state_alias("or") == "Odisha"
    assert resolve_state_alias("Or") == "Odisha"
