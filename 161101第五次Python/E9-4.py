# -*- coding: utf-8 -*-
counter = 1
num = 0


def test_varibale():
    global counter
    for I in (1, 2, 3):
        counter += 1
    num = 10


test_varibale()
print(counter, num)
# 4 0
