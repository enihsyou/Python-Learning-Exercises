# -*- coding: utf-8 -*-
def f(a, b):
    if b == 0: print(a)
    else: f(b, a % b)

print(f(9, 6))
# 3
# None
