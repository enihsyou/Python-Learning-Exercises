# -*- coding: utf-8 -*-
"""
File name: 02
Reference:
Introduction:
Date: 2016-09-20
Author: 黄春翔
ID: 1517440121
"""
from os import system


def main():
    inp = input("输入本金和利率 以半角空格分隔 如'100 0.1'\n>>>")
    try:
        a, b = map(float, inp.split())
        assert isinstance(a, float)
        assert isinstance(b, float)
    except (AssertionError, Exception):
        print("输入错误")
    else:
        print(a * (1 + b))


if __name__ == "__main__":
    main()
    system("pause")
