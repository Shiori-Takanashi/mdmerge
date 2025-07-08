# scripts/main.py
# -*- coding: utf-8 -*-

from __future__ import annotations
import click
from pathlib import Path
from typing import List, Dict, Tuple
from const.emoji import EMOJI_LIST

TECH_DIR = Path(r"C:\Users\ns69a\Documents\Obsidians\tech")
IGNORE_DIRS = [".trash", ".obsidian"]


@click.command()
def run():
    """Run the mdmerge command."""
    click.echo("ディレクトリ一覧")
    dirpaths = dir_search(TECH_DIR)
    dirnames = make_display_text(dirpaths)
    if not dirnames:
        pass


def make_display_text(dirnames: List[str]) -> List[str]:
    """ディレクトリ名のリストを表示用のテキストに変換する関数."""
    pass


def dir_search(path: Path) -> list[Path]:
    """ディレクトリを検索して一覧を返す関数."""
    return [d for d in path.iterdir() if d.is_dir() and d.name not in IGNORE_DIRS]


def add_space_to_emoji(dirnames: List[str], emoji_list: List[str] = EMOJI_LIST) -> str:
    """テキスト内の絵文字の前後にスペースを追加する関数."""
    results = []
    for dirname in dirnames:
        for emoji in emoji_list:
            if emoji in dirname:
                dirname = dirname.replace(emoji, f" {emoji} ")
        results.append(dirname)
    return results


if __name__ == "__main__":
    run()
