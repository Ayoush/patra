"""Tests for the full normalisation pipeline."""
import re

import pytest

from patra.errors import PatraError
from patra.pipeline import normalise


def test_basic_normalisation():
    result = normalise("andheri west", "MH", "400053")
    assert result.locality == "Andheri West"
    assert result.state == "Maharashtra"
    assert result.pincode == "400053"
    assert result.state_was_alias is True


def test_whitespace_collapsed():
    result = normalise("  koramangala  4th block  ", "KA", "560034")
    assert result.locality == "Koramangala 4Th Block"
    assert result.state == "Karnataka"


def test_canonical_state_not_marked_alias():
    result = normalise("Bandra", "Maharashtra", "400050")
    assert result.state_was_alias is False


def test_invalid_pincode_raises():
    with pytest.raises(PatraError) as exc_info:
        normalise("Andheri", "MH", "040001")
    assert exc_info.value.code == "INVALID_PINCODE"


@pytest.mark.parametrize("bad_pincode", ["040001", "12345", "40005A"])
def test_invalid_pincode_message_includes_value(bad_pincode):
    expected = re.escape(f"[INVALID_PINCODE] '{bad_pincode}' is not a valid Indian pincode")
    with pytest.raises(PatraError, match=expected):
        normalise("Andheri", "MH", bad_pincode)


def test_empty_locality_raises():
    with pytest.raises(PatraError) as exc_info:
        normalise("", "MH", "400001")
    assert exc_info.value.code == "EMPTY_FIELD"


def test_empty_state_raises():
    with pytest.raises(PatraError) as exc_info:
        normalise("Bandra", "", "400050")
    assert exc_info.value.code == "EMPTY_FIELD"


@pytest.mark.parametrize(
    ("locality", "state", "pincode", "field"),
    [
        ("", "MH", "400001", "locality"),
        ("Bandra", "", "400050", "state"),
        ("Bandra", "MH", "", "pincode"),
    ],
)
def test_empty_field_message_names_the_field(locality, state, pincode, field):
    expected = re.escape(f"[EMPTY_FIELD] {field} must not be blank")
    with pytest.raises(PatraError, match=expected):
        normalise(locality, state, pincode)


def test_historical_alias():
    result = normalise("Fort", "Bombay", "400001")
    assert result.state == "Maharashtra"
    assert result.state_was_alias is True


def test_uk_alias():
    result = normalise("Mussoorie", "UK", "248179")
    assert result.state == "Uttarakhand"
