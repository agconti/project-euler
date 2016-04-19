def test_get_sum_even_fib_terms():
    assert get_sum_even_fib_terms(10) == 10


def fibonacci(limit):
    a = 0
    b = 1

    while a < limit:
        if a % 2 == 0:
            yield a

        a, b = b, a + b


def get_sum_even_fib_terms(n):
    return sum(i for i in fibonacci(n))
