# -*- coding: utf-8 -*-
a = {i: i ** 2 for i in range(10)}
if 3 in a:
    print("Yes, 3 is in this dict")
if 10 not in a:
    print("10 is not in this dict")
