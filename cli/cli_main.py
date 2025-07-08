# cli/cli_main.py
# -*- coding: utf-8 -*-

import click
from pathlib import Path
from scripts.core import dir_search, get_directory_names, TECH_DIR


@click.command()
def run():
    """Run the mdmerge command."""
    click.echo("ディレクトリ一覧")
    dirnames = get_directory_names(rootpath=TECH_DIR)
    click.echo("\n".join(dirnames))


if __name__ == "__main__":
    run()
