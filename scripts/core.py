# scripts/core.py
# -*- coding: utf-8 -*-

from pathlib import Path
import re
from typing import List
from const.emoji import EMOJI_LIST
from const.dirs import TECH_DIR, IGNORE_DIRS


def dir_search(rootpath: Path) -> list[Path]:
    """ディレクトリを検索して一覧を返す関数."""
    return [d for d in rootpath.iterdir() if d.is_dir() and d.name not in IGNORE_DIRS]


def get_directory_names(rootpath: Path) -> List[str]:
    """ディレクトリ名のリストを返す関数."""
    dirpaths = dir_search(rootpath=rootpath)
    return [dp.name for dp in dirpaths]
