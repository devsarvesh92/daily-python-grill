import pytest
from src.search_rotated_array import search_rotated_array

pytestmark = pytest.mark.searchrotatedarray


def test_search_rotated_array():
    assert 4 == search_rotated_array(nums=[3, 4, 5, 6, 1, 2], target=1)
