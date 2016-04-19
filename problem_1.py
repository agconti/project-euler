def test_sum_of_multiples_three_five():
    assert sum_of_multiples_three_five(10) == 23


def multiples_three_five_sequence(limit):
    for i in xrange(limit):
        if i % 5 == 0 or i % 3 == 0:
            yield i


def sum_of_multiples_three_five(n):
    """
    Calculates the sum of the all the multiples of 3 or 5 of `n`.
    @param n -- a non-negative integer
    @return integer
    """
    return sum(multiples_three_five_sequence(n))
