import pytest

def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


@pytest.mark.parametrize(
    ("input", "expected"), [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (10, 55)]
)
def test_fib(input: int, expected: int):
    assert fib(input) == expected
