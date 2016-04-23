def test_get_smallest_evenly_divisible_by():
    assert get_smallest_evenly_divisible_by(1, 10) == 2520


def is_evenly_divisible(value, low, high):
    high += 1
    for i in range(low, high):
        if value % i != 0:
            return False
    return True


def infite_seq():
    i = 1

    while True:
        yield i
        i += 1


def get_smallest_evenly_divisible_by(low, high):
    for i in infite_seq():
        if is_evenly_divisible(i, low, high):
            return i
