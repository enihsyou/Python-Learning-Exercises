# -*- coding: utf-8 -*-
import datetime

today = datetime.date(2016, 11, 29)
graduate_day = datetime.date(2019, 7, 31)
print("从{}开始到{}毕业(含两端)，其中可以在上海理工大学生活、学习{}天".format(
    today, graduate_day, (graduate_day - today).days + 1))
