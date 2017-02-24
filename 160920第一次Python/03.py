# -*- coding: utf-8 -*-
"""
File name: 03
Reference:
Introduction:
Date: 2016-09-20
Author: 黄春翔
ID: 1517440121
"""
import math

from os import system


def sstr(item):
    return "x=" + str(item)


def main():
    print("解一元二次方程：x^2-10x+16==0")
    a, b, c = 1, -10, 16
    d = b ** 2 - 4 * a * c
    if d >= 0:
        q = (math.sqrt(d) - b) / 2 * a
        w = (-math.sqrt(d) - b) / 2 * a
        print("解为" + ",".join(map(sstr, list({q, w}))))
    else:
        print("无解")


if __name__ == "__main__":
    main()
    system("pause")

