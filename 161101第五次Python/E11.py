# -*- coding: utf-8 -*-

def factorial1(n):
    if n >= 2:
        return n * factorial1(n - 1)
    return 1


factorial2 = lambda n: n * factorial2(n - 1) if n >= 2 else 1
factorial3 = lambda n: n >= 2 and n * factorial3(n - 1) or 1
print(factorial1(10))
print(factorial2(10))
print(factorial3(10))
# 3628800
