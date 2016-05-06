"""
File name: Days Between
Reference: https://checkio.org/mission/days-diff/
Time: 2016-05-05
By: enihsyou
"""
import datetime


def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    # one = datetime.date(*date1)
    # two = datetime.date(*date2)
    # return abs((two - one).days)
    return abs(datetime.date(*date1) - datetime.date(*date2)).days


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
