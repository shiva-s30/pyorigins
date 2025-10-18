import typer

from src import __version__

app = typer.Typer(help=f"Pyorigins CLI v{__version__}")

class Main:
  def __init__(self) -> None:
    pass

  def run(self) -> None:
    pass

@app.callback(invoke_without_command=True)
def main(
  ctx: typer.Context, v: bool = typer.Option(None, "--version", "-v", is_eager=True,
    help="Show version", hidden=True)):
  """PyOrigins CLI"""
  if v:
    version()
    raise typer.Exit()
  if ctx.invoked_subcommand is None:
    typer.echo(ctx.get_help())
    raise typer.Exit()

@app.command()
def version():
  if isinstance(__version__, str) and __version__ != "":
    typer.echo(__version__)
    raise typer.Exit()

@app.command()
def run(
  option: bool = typer.Option(False, "-o", help="option help")):

  if option:
    pass

  print("Pyorigins says hello!")


if __name__ == "__main__":
  app()
