import pytest

from workshop_08.largest_triple_product import find_max_product


def test_always_passes():
    assert True


def test_always_fails():
    with pytest.raises(AssertionError):
        assert False


@pytest.mark.parametrize("data,expected_output",
    [
        ([1, 2, 3, 4, 5], [-1, -1, 6, 24, 60]),
        ([2, 4, 7, 1, 5, 3], [-1, -1, 56, 56, 140, 140]),
    ]
)
def test_find_max_product(data, expected_output):
    assert find_max_product(data) == expected_output
