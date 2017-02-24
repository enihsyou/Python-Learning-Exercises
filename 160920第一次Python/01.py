# -*- coding: utf-8 -*-
"""
File name: 01
Reference:
Introduction:
Date: 2016-09-20
Author: 黄春翔
ID: 1517440121
"""
from os import system


def C2F(degree):
    degree = int(degree)
    return str((9 / 5.0) * degree + 32) + 'F'


def F2C(degree):
    degree = int(degree)
    return str((degree - 32) * (5 / 9.0)) + 'C'


def main():
    inp = input("输入要转换的温度，以‘C'或者'F'结尾\n>>>")
    if inp.endswith('C'):
        func = C2F
    elif inp.endswith('F'):
        func = F2C
    else:
        func = None
    try:
        print(func(inp[:-1]))
    except (TypeError, Exception):
        print('输入不正确')
        main()
        return


if __name__ == "__main__":
    main()
    system("pause")
