"""Console script for tme_project_omar."""
import tme_project_omar

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for tme_project_omar."""
    console.print("Replace this message by putting your code into "
               "tme_project_omar.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
