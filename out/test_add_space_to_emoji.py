# tests/test_add_space_to_emoji.py
# -*- coding: utf-8 -*-

from __future__ import annotations
import pytest
from pathlib import Path
from typing import List, Dict, Tuple
from scripts.main import add_space_to_emoji


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
    """Test adding spaces around emojis in directory names."""
    expected_results: List[str] = [
        "test_dir 😊",
        "another_dir 🚀",
        "emoji_test 🐍",
        "no_emoji_here",
        "multiple_emojis 😊 🚀",
        "emoji_at_end 🚀 ",
        "😊 test_dir",
        "",
    ]

    results = add_space_to_emoji(sample_dirnames)

    assert (
        results == expected_results
    ), f"Expected {expected_results}, but got {results}"


if __name__ == "__main__":
    pytest.main([__file__])
