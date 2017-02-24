# -*- coding: utf-8 -*-
a = {i: i ** 2 for i in range(10)}
print(a.keys())
print(a.values())
for key, item in a.items():
    print(key, item)
