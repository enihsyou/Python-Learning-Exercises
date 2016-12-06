# -*- coding: utf-8 -*-
def is_leap_year(year):
    # if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    #     return True
    # return False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    print("是闰年" if is_leap_year(int(input("输入年份："))) else "不是闰年")
    print("\n本世纪有", sum(((print(year, end=' ') or 1)
                         if is_leap_year(year) else 0
                         for year in range(2000, 2099))), "个闰年")
