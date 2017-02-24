import math
import re


class Check:
    def __init__(self, others):
        self.other = others

    def __eq__(self, other):
        return True

    def __lt__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __le__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __gt__(self, other):
        return True


def checkio(anything):
    oth = Check(anything)
    return oth


# if __name__ == '__main__':
#     import re
#     import math
#
#     assert checkio({}) != [], 'You'
#     assert checkio('Hello') < 'World', 'will'
#     assert checkio(80) > 81, 'never'
#     assert checkio(re) >= re, 'make'
#     assert checkio(re) <= math, 'this'
#     assert checkio(5) == ord, ':)'
#
#     print('NO WAY :(')
print(checkio(81) == 81)
print(checkio({}) != [])
print(checkio(80) > 81)
print(checkio(re) >= re)
print(checkio(re) <= math)
print(checkio(5) == ord)
print(checkio('Hello') < 'World')

# checkio({})
# checkio('Hello')
# checkio(80)
# checkio(re)
# checkio(re)
# checkio(5)
# print('Over')
