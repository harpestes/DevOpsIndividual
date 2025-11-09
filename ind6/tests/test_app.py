import pytest
from ind6.app import add, is_even


def test_add_simple():
    assert add(2, 3) == 5
    assert add(-1, 1.5) == 0.5
    assert add(0, 0) == 0


@pytest.mark.parametrize("value, expected", [
    (7, False),
    (4, True),
    (9, False),
    (1.1, False),
])
def test_is_even(value, expected):
    assert is_even(value) == expected
