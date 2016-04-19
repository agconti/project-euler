def test_frizz_buzz():
    assert frizz_buzz(10) == 23
    

def frizz_buzz(number):
    """
    Calculates the sum of the all the multiples of 3 or 5 of `n`.
    @param n -- a non-negative integer
    @return integer
    """
    mutliples_of_three_and_five = lambda x: (x % 5 == 0) or (x % 3 == 0)
    return sum(filter(mutliples_of_three_and_five, range(number)))
