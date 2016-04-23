def test_sum_square_difference():
    assert sum_square_difference(1, 10) == 2640


def sum_square_difference(low, high):
    high += 1

    sum_squares = pow(sum(xrange(low, high)), 2)
    square_sum = sum(map(lambda num: pow(num, 2), xrange(low, high)))
    return sum_squares - square_sum
