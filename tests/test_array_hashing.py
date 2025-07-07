import pytest

from src.array_hashing import (
    group_anagrams,
    longest_consecutive_sequence,
    top_k_frequent_elements,
    product_of_array_execept_self,
)


pytestmark = pytest.mark.array_hashing


def test_group_anagram():
    assert [["act", "cat"], ["pots", "tops", "stop"], ["hat"]] == group_anagrams(
        input=["act", "pots", "tops", "cat", "stop", "hat"]
    )


def test_top_k_frequent_elements():
    assert [3, 2] == top_k_frequent_elements(k=2, nums=[1, 2, 2, 3, 3, 3])


def test_product_of_array_except_self():
    assert [48, 24, 12, 8] == product_of_array_execept_self(nums=[1, 2, 4, 6])


def test_longest_consecutive_sequence():
    assert 4 == longest_consecutive_sequence(nums=[2, 20, 4, 10, 3, 4, 5])
