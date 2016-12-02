# -*- coding: utf-8 -*-
def is_leap_year(year):
    # if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    #     return True
    # return False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print("本世纪有", sum(((print(year) or 1)
                   if is_leap_year(year) else 0
                   for year in range(2000, 2099))), "个闰年")
