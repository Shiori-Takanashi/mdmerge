# tests/test_add_space_to_emoji.py
# -*- coding: utf-8 -*-


import pytest
from typing import List
from scripts.main import add_space_to_emoji
from tests.emoji_mock import EMOJI_LIST


@pytest.fixture
def sample_dirnames() -> List[str]:
    """Sample directory names for testing."""
    return [
        "test_dir 😊",
        "another_dir 🚀",
        "emoji_test 🐍",
        "no_emoji_here",
        "multiple_emojis 😊🚀",
        "emoji_at_end 🚀",
        "emoji_at_start 😊test_dir",
        "",
    ]


def test_add_space_to_emoji(sample_dirnames: List[str]) -> None:
    expected_results: List[str] = [
        "test_dir 😊",
        "another_dir 🚀",
        "emoji_test 🐍",
        "no_emoji_here",
        "multiple_emojis 😊 🚀",
        "emoji_at_end 🚀",  # ← 末尾スペース不要
        "emoji_at_start 😊 test_dir",  # ← emoji の位置はそのまま
        "",
    ]

    results = add_space_to_emoji(sample_dirnames, emoji_list=EMOJI_LIST)  # モックを指定

    assert (
        results == expected_results
    ), f"Expected {expected_results}, but got {results}"


if __name__ == "__main__":
    pytest.main([__file__])
