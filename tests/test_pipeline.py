"""Tests for the full normalisation pipeline."""
import pytest
from patra.pipeline import normalise
from patra.errors import PatraError


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


def test_empty_locality_raises():
    with pytest.raises(PatraError) as exc_info:
        normalise("", "MH", "400001")
    assert exc_info.value.code == "EMPTY_FIELD"


def test_empty_state_raises():
    with pytest.raises(PatraError) as exc_info:
        normalise("Bandra", "", "400050")
    assert exc_info.value.code == "EMPTY_FIELD"


def test_historical_alias():
    result = normalise("Fort", "Bombay", "400001")
    assert result.state == "Maharashtra"
    assert result.state_was_alias is True


def test_uk_alias():
    result = normalise("Mussoorie", "UK", "248179")
    assert result.state == "Uttarakhand"
