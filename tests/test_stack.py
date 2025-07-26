import pytest

from src.stack import valid_parentheses


pytestmark = pytest.mark.stack


def test_valid_parentheses():
    assert True == valid_parentheses(input="([{}])")
