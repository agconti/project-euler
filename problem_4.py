def test_largest_palindrome():
    assert largest_palindrome(100, 10) == 9009


def get_all_products_of_value_to_limt(value, limit):
    for i in reversed(xrange(limit, value)):
        yield i * value


def largest_palindrome(n, limit):
    for i in reversed(xrange(n)):
        for value in get_all_products_of_value_to_limt(i, limit):
            value = str(value)
            if value == value[::-1]:
                return int(value)
