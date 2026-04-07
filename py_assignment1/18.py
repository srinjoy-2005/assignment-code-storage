import pytest

# The function to be tested
def compute_power(base, exponent):
    return base ** exponent

test_data = [
    (2, 2, 4),
    (2, 3, 8),
    (1, 9, 1),
    (0, 9, 0),
]

@pytest.mark.parametrize("base, exponent, expected", test_data)
def test_power_values(base, exponent, expected):

    assert compute_power(base, exponent) == expected