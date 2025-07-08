# scripts/main.py
# -*- coding: utf-8 -*-

import click
from pathlib import Path
import re
from typing import List
from const.emoji import EMOJI_LIST

TECH_DIR = Path(r"C:\Users\ns69a\Documents\Obsidians\tech")
IGNORE_DIRS = [".trash", ".obsidian"]


def make_display_text(dirnames: List[str]) -> List[str]:
    """ディレクトリ名のリストを表示用のテキストに変換する関数."""
    pass


def dir_search(path: Path) -> list[Path]:
    """ディレクトリを検索して一覧を返す関数."""
    return [d for d in path.iterdir() if d.is_dir() and d.name not in IGNORE_DIRS]


def add_space_to_emoji(dirnames: List[str], emoji_list: List[str]) -> List[str]:
    results = []
    for name in dirnames:
        new = name
        for e in emoji_list:
            # 前にスペースがなければ付ける
            new = re.sub(rf"(?<!\s){re.escape(e)}", r" \g<0>", new)
            # 後ろにスペースがなければ付ける
            new = re.sub(rf"{re.escape(e)}(?!\s)", r"\g<0> ", new)
        # 連続スペースを 1 つに、行頭尾のスペースを除去
        new = re.sub(r" +", " ", new).strip()
        results.append(new)
    return results


@click.command()
def run():
    """Run the mdmerge command."""
    click.echo("ディレクトリ一覧")
    dirpaths = dir_search(TECH_DIR)
    dirnames = make_display_text(dirpaths)
    if not dirnames:
        pass


if __name__ == "__main__":
    run()
