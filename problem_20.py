def test_factorial_digit_sum():
    assert factorial_digit_sum(10) == 27


def factorial_digit_sum(n):
    n_factorial_iterable = str(math.factorial(n))
    digits_in_n_factorial = [int(i) for i in n_factorial_iterable]
    return sum(digits_in_n_factorial)
