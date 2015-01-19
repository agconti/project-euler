"""
# 1. Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def test_frizz_buzz():
    assert frizz_buzz(10) == 23
    assert frizz_buzz(1000) == 233168


def frizz_buzz(number):
    """
    Calculates the sum of the all the multiples of 3 or 5 of `n`.
    @param n -- a non-negative integer
    @return integer
    """
    mutliples_of_three_and_five = lambda x: (x % 5 == 0) or (x % 3 == 0)
    return sum(filter(mutliples_of_three_and_five, range(number)))
