import pytest

def power(a, b):
    if a == 0 and b == 0:
        raise ValueError("0^0 is undefined")
    return a ** b


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (2, 3, 8),
    (1, 9, 1),
    (0, 9, 0),
])
def test_power_valid(a, b, expected):
    assert power(a, b) == expected


def test_power_error():
    with pytest.raises(ValueError):
        power(0, 0)