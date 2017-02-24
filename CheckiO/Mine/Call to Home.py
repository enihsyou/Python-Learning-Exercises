"""
File name: Call to Home
Reference: https://checkio.org/mission/calls-home/
Time: 2016-05-07
By: enihsyou
"""
import math
from collections import namedtuple


def total_cost(calls):
    base = namedtuple('calls', ['date', 'time', 'duration'])
    call = [base(*i.split()) for i in calls]
    nowdate = call[0].date
    today_100 = 100
    fee = 0
    for item in call:
        duration = math.ceil(int(item.duration) / 60)
        if item.date != nowdate:
            nowdate = item.date
            today_100 = 100
        while today_100 and duration:
            today_100 -= 1
            duration -= 1
            fee += 1
        while duration:
            duration -= 1
            fee += 2
    print(fee)
    return fee


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
