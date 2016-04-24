def test_triangle_number_factors():
    assert  get_triangle_number_with_factors_greater_than(5) == 28


# o(n), theta(n), omega(n)
def get_triangle_number(n):
    start = 1
    end = n + 1
    return sum(xrange(start, end))


# o(n), theta(n), omega(1)
def num_factors_over_limit(num, limit):
    end = num + 1
    num_factors = 0
    for i in xrange(1, end):
        if num % i  == 0:
            num_factors += 1
        if num_factors > limit:
            return True
    return False


# o(1), theta(1), omega(1)
def infinite_triangle_number_seq(start):
    num = start

    while True:
        yield get_triangle_number(num)
        num += 1


# o(n), theta(n), omega(n)
def get_triangle_number_with_factors_greater_than(n):
    for i in infinite_triangle_number_seq(n):
        if num_factors_over_limit(i, n):
            return i
