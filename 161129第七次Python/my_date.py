# -*- coding: utf-8 -*-
class Date:
    def __init__(self, year: int = 1970, month: int = 1, day: int = 1):
        self.year = year
        self.month = month
        self.day = day


class Time:
    def __init__(self, hour: int = 0,
                 minute: int = 0,
                 second: int = 0,
                 millisecond: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond


class DateTime:
    def __init__(self, year: int = 1970,
                 month: int = 1,
                 day: int = 1,
                 hour: int = 0,
                 minute: int = 0,
                 second: int = 0,
                 millisecond: int = 0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
