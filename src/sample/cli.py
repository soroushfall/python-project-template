from __future__ import annotations

from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def hello(name: Annotated[str, typer.Argument(help="Your name")]) -> None:
    """Say hi—replace me with your real CLI entrypoints."""
    typer.echo(f"Hello, {name}!")


def run() -> None:
    app()


if __name__ == "__main__":
    run()
