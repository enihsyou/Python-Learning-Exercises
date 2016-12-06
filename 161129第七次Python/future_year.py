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
format_pattern = "%Y-%m-%d"

if __name__ == '__main__':
    input_date = input("输入年-月-日(2016-12-06)：")
    try:
        input_date_parsed = datetime.datetime.strptime(
            input_date if input_date.strip()
            else datetime.date.today().strftime(format_pattern),
            format_pattern)
    except ValueError:
        print("输入格式有误")
    else:
        print("{}是星期{}".format(
            input_date_parsed.strftime(format_pattern),
            day_to_chinese[input_date_parsed.weekday()]))
    finally:
        this_year = datetime.datetime.now().year
        for year in range(this_year, this_year + 100):
            birthday = datetime.date(year, 3, 9)
            print("{}年的生日是星期{}".format(
                year, day_to_chinese[birthday.weekday()]))
