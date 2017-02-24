# -*- coding: utf-8 -*-
"""
File name: 05
Reference:
Introduction:
Date: 2016-09-20
Author: 黄春翔
ID: 1517440121
"""
import math

from os import system


class Triangle:
    def __init__(self, a, b, c, *args):
        p = sum([a, b, c]) / 2
        self.area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __str__(self):
        return str(self.area)


def main():
    print("三角形面积为",
          Triangle(*map(float, input("输入三条边 以空格分隔\n>>>").split())))


if __name__ == "__main__":
    main()
    system("pause")
