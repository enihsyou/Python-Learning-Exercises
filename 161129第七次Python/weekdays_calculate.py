# -*- coding: utf-8 -*-
import datetime

today = datetime.date(2016, 11, 29)
holiday = today + datetime.timedelta(48)
print("今天是{}，距离放假还有48天，放假那天是{}, {}".format(
    today, holiday, holiday.strftime("%A")))
