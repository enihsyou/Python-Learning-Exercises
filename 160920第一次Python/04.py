# -*- coding: utf-8 -*-
"""
File name: 04
Reference:
Introduction:
Date: 2016-09-20
Author: 黄春翔
ID: 1517440121
"""
import datetime

from os import system


def main():
    name = input("输入姓名\n>>>")
    date = input("输入出身年份\n>>>")
    thisyear = datetime.date.today().year
    try:
        date = int(date)
        if date > thisyear:
            print("不科学")
            return 
    except ValueError:
        print('输入的年份不合法')
    else:
        print("""你好！{} 你 {} 岁""".format(name, thisyear.year - date))


if __name__ == "__main__":
    main()
    system("pause")
