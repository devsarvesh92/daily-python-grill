import pytest

from src.binary_search import binary_search


pytestmark = pytest.mark.binary_search


def test_binary_search():
    assert 1 == binary_search(ls=[3, 4, 5, 6], num=4)
