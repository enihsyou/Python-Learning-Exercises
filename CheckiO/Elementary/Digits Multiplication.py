"""
File name: Digits Multiplication
Reference: https://checkio.org/mission/digits-multiplication/
Time: 2016-05-04
By: enihsyou
"""


def checkio(number):
    from functools import reduce
    return int(reduce(lambda x, y: int(x) * int(y), str(number).replace('0', '')))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
