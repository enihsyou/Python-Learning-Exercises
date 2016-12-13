# -*- coding: utf-8 -*-
from functools import reduce


def array_add(a, b):
    return [q + w for q, w in zip(a, b)]


def array_sub(a, b):
    return [q - w for q, w in zip(a, b)]


def array_ge(a, b):
    """a >= b"""
    return all(i >= j for i, j in
    zip(a, b))  # and not all(i == j for i, j in zip(a, b))


def input_resources():
    while True:
        try:
            n_resources = int(input("Input number of resources: "))
        except ValueError:
            continue
        else:
            return n_resources


def input_processes():
    while True:
        try:
            n_processes = int(input("Input number of processes: "))
        except ValueError:
            continue
        else:
            return n_processes


def input_system_resource():
    """输入系统资源总数"""
    while True:
        try:
            return [int(x) for x in
                input("Input system resources: ").strip().split()[:N_RESOURCES]]
        except ValueError:
            continue


def input_allocated():
    while True:
        try:
            return [[int(x) for x in input(
                "Input current allocated for P%d: " % (i + 1)).strip().split()[
            :N_RESOURCES]]
                for i in
                range(N_PROCESSES)]
        except ValueError:
            print("Something wrong")


def input_demand():
    while True:
        try:
            return [[int(x) for x in
                input("Input max demand for P%d: " % (i + 1)).strip().split()[
                :N_RESOURCES]] for i in range(N_PROCESSES)]
        except ValueError:
            print("Something wrong")


def input_request():
    while True:
        try:
            index = int(input("Please input the customer's index: "))
            return index, [int(x) for x in
                input("Please input P%d's requests: " % index).strip().split()[
                :N_RESOURCES]]
        except ValueError:
            print("Something wrong")


def calc_total_resources(available, allocated):
    """由可用向量和已分配矩阵 计算资源总量，用可用加上已分配的 对列分别求和"""
    # return [available[column] + sum(row[column] for row in allocated) for column in range(len(allocated[0]))]
    return reduce(array_add, allocated, available)


def calc_available_available(total, allocated):
    """由总量向量和已分配矩阵 计算可用向量，用总量减去已分配的 对列分别求差"""
    return reduce(array_sub, allocated, total)


# 输入资源维度
# n_resources = input_resources()
N_RESOURCES = 3
# 输入进程数量
# n_processes = input_processes()
N_PROCESSES = 5
# 输入资源总量
# total_resources = input_system_resource()
TOTAL_RESOURCES = [10, 5, 7]
# 输入每进程最大需求量
# max_demand = input_demand()
MAX_DEMAND = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
# 输入每进程当前分配量
# current_allocated = input_allocated()
current_allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
# 计算当前可用资源量
current_available = calc_available_available(TOTAL_RESOURCES, current_allocated)


def system_security():
    total = current_available
    order = []
    print_header()  # print table header

    running = [1 for _ in range(N_PROCESSES)]  # 标记进程正在运行
    while running.count(0) != N_PROCESSES:  # 如果所有进程都没有完成
        try_allocated = False  # 尝试分配标记
        for process in range(N_PROCESSES):  # 对于每个进程
            # 如果 对于当前进程 所有资源的可用量大于需求量
            new_allocate = array_sub(MAX_DEMAND[process],
                current_allocated[process])
            if all(i >= 0 for i in array_sub(total, new_allocate)) and running[
                process]:
                # 当前进程分配成功
                try_allocated = True
                # 标记完成
                running[process] = 0
                order.append(process)
                finish = print_item(process, total, new_allocate,
                    current_allocated[process])
                # 进程完成 释放资源
                total = finish
        if not try_allocated:  # 如果一轮过去都没有分配成功，则失败了
            print("SYSTEM INSECURITY")
            return False
    print("SYSTEM SECURITY")
    return True


def print_header():
    print("{:<12s}{:<12s}{:<12s}{:<12s}{:<8s}".format("Process", "Available",
        "Allocated", "Working", "Finish"))


def print_item(process, available, allocated, working):
    """
    :param process 进程序号
    :param available 当前可用资源量
    :param allocated 被分配的量
    :param working 原先已占有的资源量

    :rtype list[int] 进程完成之后，系统可用资源量
    """
    finish = array_add(available, working)
    print(
        "P{:<11d}{:<12s}{:<12s}{:<12s}{:<8s}".format(process, str(available),
            str(allocated), str(working),
            str(finish)))
    return finish


def print_available():
    print("{:>56}".format(str(current_available)))


def try_allocate(index, request):
    global current_allocated, current_available
    current_available = array_sub(current_available, request)  # 可用量减少
    current_allocated[index] = array_add(current_allocated[index],
        request)  # 进程分配量增加


def request_security():
    global current_allocated, current_available
    index, request = input_request()
    # assert 小于需求量
    if not array_ge(array_sub(MAX_DEMAND[index], current_allocated[index]),
            request):
        print("RESOURCE OVERLOADED")
        return False
    # assert 小于可用量
    if not array_ge(current_available, request):
        print("RESOURCE INSUFFICIENT")
        return False
    # 保存状态
    current_state = [current_allocated, current_available]
    # 预分配
    try_allocate(index, request)
    if system_security():
        print("CUSTOMER P%d CAN GET RESOURCES IMMEDIATELY" % index)
        # current_allocated, current_available = current_state
        return True
    else:
        print("CUSTOMER P%d CANNOT OBTAIN RESOURCES IMMEDIATELY" % index)
        current_allocated, current_available = current_state
        return False


def choose_action():
    choose_dict = {1: system_security, 2: request_security, 3: quit}
    while True:
        user_input = input("1. Judge the system security.\n"
                           "2. Judge the request security.\n"
                           "3. Quit.\n")
        try:
            choose = int(user_input)
            return choose_dict[choose]
        except KeyError:
            continue


if __name__ == "__main__":
    while 1:
        action = choose_action()
        action()
