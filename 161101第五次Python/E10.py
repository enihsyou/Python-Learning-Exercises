# -*- coding: utf-8 -*-
import random

number_list = []
num = 10
for i in range(num):
    number_list.append(random.randint(0, num))
print("随机数列表:", number_list)


def mymax(list):
    def _max(num_list, pivot):
        if not num_list: return pivot
        if num_list[0] > pivot:
            pivot = num_list[0]
        return _max(num_list[1:], pivot)

    pivot = list[0]
    return _max(list, pivot)


print("内建函数max:", max(number_list), "自定义函数mymax:", mymax(number_list))
