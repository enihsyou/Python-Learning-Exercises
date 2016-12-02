# -*- coding: utf-8 -*-
import datetime

day_to_chinese = {
    0: "一",
    1: "二",
    2: "三",
    3: "四",
    4: "五",
    5: "六",
    6: "日",
}
this_year = datetime.datetime.now().year
for year in range(this_year, this_year + 100):
    birthday = datetime.date(year, 3, 9)
    print("{}年的生日是星期{}".format(year, day_to_chinese[birthday.weekday()]))
