"""Console script for pystaticrypt."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("pystaticrypt")
    click.echo("=" * len("pystaticrypt"))
    click.echo("Encrypt static html for client-side password access (unsafe for production usage)")


if __name__ == "__main__":
    main()  # pragma: no cover
