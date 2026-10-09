"""CLI entry point for patra."""
import json
import sys

import typer

from .pipeline import normalise
from .errors import PatraError

app = typer.Typer(name="patra", help="Normalise Indian address fields.")


@app.command()
def run(
    locality: str = typer.Argument(..., help="Locality / city / village"),
    state: str = typer.Argument(..., help="State name or abbreviation"),
    pincode: str = typer.Argument(..., help="6-digit Indian pincode"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
) -> None:
    """Normalise an Indian address and print the result."""
    try:
        result = normalise(locality, state, pincode)
    except PatraError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(code=1) from e

    if json_output:
        typer.echo(
            json.dumps(
                {
                    "locality": result.locality,
                    "state": result.state,
                    "pincode": result.pincode,
                    "state_was_alias": result.state_was_alias,
                }
            )
        )
    else:
        typer.echo(f"{result.locality}, {result.state} {result.pincode}")
        if result.state_was_alias:
            typer.echo(f"  (state resolved from alias: '{result.raw_state}' -> '{result.state}')")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
