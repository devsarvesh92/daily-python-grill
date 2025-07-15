import pytest

from src.two_pointers import valid_palindrome


pytestmark = pytest.mark.two_pointers


def test_valid_palindrome():
    assert True == valid_palindrome(s="Was it a car or a cat I saw?")
