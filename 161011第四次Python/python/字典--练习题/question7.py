# -*- coding: utf-8 -*-
a = {number + 1: item for number, item in
     enumerate([
         'Monday',
         'Tuesday',
         'Wednesday',
         'Thursday',
         'Friday',
         'Saturday ',
         'Sunday', ])}
print(a.keys())
print(a.values())
print(a.items())
