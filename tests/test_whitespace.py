"""Tests for whitespace normalisation."""
from patra.whitespace import normalise_whitespace


def test_strips_leading_trailing():
    assert normalise_whitespace("  hello  ") == "hello"


def test_collapses_internal_whitespace():
    assert normalise_whitespace("hello   world") == "hello world"


def test_handles_tabs_and_newlines():
    assert normalise_whitespace("hello\tworld\n") == "hello world"


def test_empty_string_stays_empty():
    assert normalise_whitespace("") == ""


def test_only_whitespace_becomes_empty():
    assert normalise_whitespace("   \t  ") == ""
