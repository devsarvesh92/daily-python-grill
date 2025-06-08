


import pytest

from src.array_hashing import group_anagrams, top_k_frequent_elements


pytestmark = pytest.mark.array_hashing


def test_group_anagram():
    assert [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']] == group_anagrams(input=["act","pots","tops","cat","stop","hat"])

def test_top_k_frequent_elements():
    assert [3,2] == top_k_frequent_elements(k=2,nums=[1,2,2,3,3,3])
