
import json
from pathlib import Path

import pytest

from patra.pipeline import normalise


FIXTURE_PATH = (
    Path(__file__).resolve().parents[1]
    / "fixtures"
    / "golden"
    / "pipeline.json"
)


def load_cases():
    """Load golden test cases from the JSON fixture."""
    with FIXTURE_PATH.open(encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.parametrize(
    "case",
    load_cases(),
    ids=lambda case: (
        case["input"].get("locality", "unknown-locality").strip()
        or "empty-locality"
    ),
)
def test_pipeline_golden(case):
    """Check normalized output against expected golden values."""
    actual = normalise(**case["input"])

    for field, expected_value in case["expected"].items():
        assert getattr(actual, field) == expected_value, (
            f"Mismatch for locality "
            f"{case['input'].get('locality')!r}, field {field!r}: "
            f"expected {expected_value!r}, "
            f"got {getattr(actual, field)!r}"
        )
