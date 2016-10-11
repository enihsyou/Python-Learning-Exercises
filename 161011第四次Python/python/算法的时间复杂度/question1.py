# -*- coding: utf-8 -*-


def ten2(number, base):
    """进制转换"""
    result = []
    while number:
        number, a = divmod(number, base)
        result.append(str(a))
    result.reverse()
    return ''.join(result)


for i in range(100, 1000):
    if ten2(i, 7) == ten2(i, 9)[::-1]:  # 数码顺序正好相反
        print(i)

# i = 248
input()
