"""Pincode validation and prefix lookup."""
import re

_PINCODE_RE = re.compile(r"^[1-9][0-9]{5}$")

# Zone prefixes: digit 1 of pincode -> region
PINCODE_ZONES: dict[str, str] = {
    "1": "Delhi, Haryana, Punjab, HP, J&K",
    "2": "UP, Uttarakhand",
    "3": "Rajasthan, Gujarat",
    "4": "Maharashtra, MP, Chhattisgarh",
    "5": "AP, Telangana, Karnataka",
    "6": "Tamil Nadu, Kerala",
    "7": "West Bengal, Odisha, Northeast",
    "8": "Bihar, Jharkhand, Odisha",
    "9": "APO / Military",
}


def is_valid_pincode(pin: str) -> bool:
    """Return True if pin is exactly 6 digits with no leading zero."""
    return bool(_PINCODE_RE.match(pin.strip()))


def pincode_zone(pin: str) -> str | None:
    """Return the region description for the pincode's zone digit, or None if invalid."""
    p = pin.strip()
    if not is_valid_pincode(p):
        return None
    return PINCODE_ZONES.get(p[0])
