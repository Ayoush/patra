"""Tests for pincode validation."""
from patra.pincode import is_valid_pincode, pincode_zone


def test_valid_pincode():
    assert is_valid_pincode("400001") is True


def test_rejects_leading_zero():
    assert is_valid_pincode("040001") is False


def test_rejects_too_short():
    assert is_valid_pincode("40000") is False


def test_rejects_too_long():
    assert is_valid_pincode("4000011") is False


def test_rejects_non_digits():
    assert is_valid_pincode("4000AB") is False


def test_zone_for_mumbai():
    zone = pincode_zone("400001")
    assert zone is not None
    assert "Maharashtra" in zone


def test_zone_returns_none_for_invalid():
    assert pincode_zone("040001") is None
