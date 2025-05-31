


import pytest

from src.array_hashing import group_anagrams


pytestmark = pytest.mark.array_hashing


def test_group_anagram():
    assert [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']] == group_anagrams(input=["act","pots","tops","cat","stop","hat"])

