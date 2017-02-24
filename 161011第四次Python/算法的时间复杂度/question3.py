# -*- coding: utf-8 -*-
from math import sqrt

for i in range(1000, 10000):  # 4位数
    first2 = set(str(i)[:2])  # 前两个
    if len(first2) == 1:
        last2 = set(str(i)[2:])  # 后两个
        if len(last2) == 1 and not last2 & first2:  # 首尾相等
            if int(sqrt(i)) ** 2 == i:  # 验证是一个数的平方
                print(i)
# 7744
input()
