def difference(*numbers):
    """
    Function take list of any number of digits
    and return difference between the max and min
    as a number
    :param numbers: list of numbers
    :return: int or float
    """
    return 0 if not numbers else round(max(numbers) - min(numbers), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
