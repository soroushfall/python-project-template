from __future__ import annotations

import typer
from typing import Annotated

app = typer.Typer(no_args_is_help=True)

@app.command()
def hello(name: Annotated[str, typer.Argument(help="Your name")]):
    """Say hi—replace me with your real CLI entrypoints."""
    typer.echo(f"Hello, {name}!")

def run():
    app()

if __name__ == "__main__":
    run()