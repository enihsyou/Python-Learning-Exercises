# -*- coding: utf-8 -*-
from math import sqrt

y1 = 10  # sqrt(y)
while 1:  # 存在解
    y = y1 * y1
    x = y - 100
    z = y + 68
    if int(sqrt(z)) ** 2 == z:  # 验证是一个数的平方
        print(x)
        break
    else:
        y1 += 1
# x = 156
input()
