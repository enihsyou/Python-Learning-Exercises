# -*- coding: utf-8 -*-
b = dict()
a = {i: i ** 2 for i in range(10)}
print(a.keys())
print(a.values())
for key, item in a.items():
    print(key, item)
