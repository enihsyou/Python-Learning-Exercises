# -*- coding: utf-8 -*-
"""
File name: 06
Reference:
Introduction:
Date: 2016-09-20
Author: 黄春翔
ID: 1517440121
"""
from os import system

mark = {
    range(90, 101): "优",
    range(80, 90): "良",
    range(70, 80): "中",
    range(60, 70): "及格",
    range(0, 60): "不及格",
}


def main():
    try:
        inp = int(input("输入分数\n>>>"))
    except ValueError:
        print("输入有误")
        main()
    else:
        for rang, msg in mark.items():
            if inp in rang:
                print("分数：{} 等级：{}".format(inp, msg))
                return
        print("输入有误")
        main()
if __name__ == "__main__":
    main()
    system("pause")

