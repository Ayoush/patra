"""Full normalisation pipeline for Indian address fields."""
from dataclasses import dataclass

from .whitespace import normalise_whitespace
from .alias import resolve_state_alias
from .pincode import is_valid_pincode
from .casing import title_case
from .errors import PatraError


@dataclass(frozen=True)
class NormaliseResult:
    locality: str
    state: str
    pincode: str
    raw_locality: str
    raw_state: str
    raw_pincode: str
    state_was_alias: bool


def normalise(
    locality: str,
    state: str,
    pincode: str,
) -> NormaliseResult:
    """
    Normalise Indian address fields.

    Steps (in order):
    1. Trim and collapse whitespace in all fields
    2. Resolve state aliases (OR -> Odisha, UK -> Uttarakhand, etc.)
    3. Validate pincode format (6 digits, no leading zero)
    4. Title-case locality and state

    Raises PatraError with code INVALID_PINCODE if the pincode is malformed.
    Raises PatraError with code EMPTY_FIELD if any required field is blank after trimming.
    """
    raw_locality = locality
    raw_state = state
    raw_pincode = pincode

    # Step 1: whitespace
    locality = normalise_whitespace(locality)
    state = normalise_whitespace(state)
    pincode = normalise_whitespace(pincode)

    if not locality:
        raise PatraError("EMPTY_FIELD", "locality must not be blank")
    if not state:
        raise PatraError("EMPTY_FIELD", "state must not be blank")
    if not pincode:
        raise PatraError("EMPTY_FIELD", "pincode must not be blank")

    # Step 2: alias resolution
    resolved_state = resolve_state_alias(state)
    state_was_alias = resolved_state.upper() != state.upper()
    state = resolved_state

    # Step 3: pincode validation
    if not is_valid_pincode(pincode):
        raise PatraError("INVALID_PINCODE", f"'{pincode}' is not a valid Indian pincode")

    # Step 4: casing
    locality = title_case(locality)
    state = title_case(state)

    return NormaliseResult(
        locality=locality,
        state=state,
        pincode=pincode,
        raw_locality=raw_locality,
        raw_state=raw_state,
        raw_pincode=raw_pincode,
        state_was_alias=state_was_alias,
    )
