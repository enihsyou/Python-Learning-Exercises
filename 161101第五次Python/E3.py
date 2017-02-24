# -*- coding: utf-8 -*-
def f1(p, **p2):
    print(type(p2))


f1(1, a=2)
# <class 'dict'>
