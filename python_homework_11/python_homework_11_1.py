from math import ceil
from inspect import isgenerator


def prime_generator(end: int) -> list:
    """
    Function generates a prime number to the parameter
    :param end: int param which limits numbers
    :return: prime int number
    """
    value = 2
    while value <= end:
        value_end = ceil(value / 2)
        for i in range(2, value_end + 1):
            if (value % i) == 0:
                break
        else:
            yield value
        value += 1


"""gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
"""
