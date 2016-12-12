# -*- coding: utf-8 -*-
from itertools import cycle, islice


class QueueHeader:
    def __init__(self):
        self.name = "Name"
        self.elapsed = "Elapsed"
        self.remain = "Remain"
        self.count = "Count"
        self.round = "Round"
        self.state = "State"


class QueueObject:
    def __init__(self, rounds, name="name", elapsed=0, remain=0, count=0,
                 state="Waiting"):
        self.name = name  # 名字
        self.elapsed = elapsed  # 在CPU上已经运行的时间
        self.remain = remain  # 剩余要执行的CPU时间
        self.count = count  # 被执行次数
        self.round = rounds  # 时间片大小
        self.state = state  # 当前状态
        self.total = 0  # 总计时间


def input_name_and_service_time(round_times):
    queue = []
    input_string = input(
        "Please input name and service time (input 'over' to stop):\n")
    while "over" != input_string:
        try:
            body = QueueObject(round_times)
            get = input_string.split()
            if len(get) != 2:  # 如果输入格式不对
                raise TypeError
            body.name = get[0]  # 设置名字
            body.remain = int(get[1])  # 设置预计执行时间
            queue.append(body)  # 添加
            input_string = input()  # 下一个输入
        except TypeError:
            input_string = input(
                "Please try again, a string and an integer, split by a single space:\n")
        except ValueError:
            input_string = input(
                "Please try again, service time is an integer:\n")
    queue[0].state = "Ready"
    return queue


def input_round():
    input_string = input("Please input round times:\n")
    while 1:
        try:
            round_input = int(input_string)
            if round_input <= 0:
                raise TypeError
            return round_input
        except TypeError:
            input_string = input("The number must be positive:\n")
        except ValueError:
            input_string = input("Please try again, input an integer:\n")


def print_format(queues):
    """打印当前状态内容"""
    for item in [QueueHeader()] + queues:
        print(
            "{o.name:<8}{o.elapsed:<8}{o.remain:<8}{o.count:<8}{o.round:<8}{o.state:<8}"
                .format(o=item))


def print_queue(queues):
    ready, finished, un_finished = [], [], []
    for i in queues:
        if i.state == "Finished":
            finished.append(i)
        else:
            if i.state == "Waiting":
                ready.append(i)
            un_finished.append(i)
    # 排序队列
    queues.clear()
    queues.extend(un_finished)
    queues.extend(finished)

    if ready:
        print("Ready queue: " + ", ".join(map(lambda x: x.name, ready)))
    if finished:
        print("Finished queue: " + ", ".join(map(lambda x: x.name, finished)))



def perform_next(queues, round_times):
    this = queues[0]  # type: QueueObject
    assert this.state == "Ready"
    if this.remain > round_times:  # 如果分片时间小于当前需求
        this.remain -= round_times  # 相当于进行计算
        this.elapsed += round_times  # 递增执行时间
        this.state = "Waiting"
    else:
        this.elapsed += this.remain  # 递增执行时间
        this.remain = 0  # 如果分片时间够用，计算完成
        this.state = "Finished"  # 标记完成
    this.count += 1


def main():
    print("{:-^80}".format("Round-robin Algorithm"))
    # 输入时间片大小
    # round_times = input_round()
    round_times = 2
    # 输入列表项目
    # queues = input_name_and_service_time(round_times)
    queues = [
        QueueObject(round_times, "a1", remain=3, state="Ready"),
        QueueObject(round_times, "a2", remain=2),
        QueueObject(round_times, "a3", remain=4),
        QueueObject(round_times, "a4", remain=2),
        QueueObject(round_times, "a5", remain=1),
    ]
    # 如果所有对象都没有完成，就继续循环
    while True:
        # 输出当前状态
        print_format(queues)
        # 输出队列
        print_queue(queues)
        print()
        if not all(item.state == "Finished" for item in queues):
            perform_next(queues, round_times)
            queues = list(islice(cycle(queues), 1, len(queues) + 1))  # 轮转列表
            # 设置第一个准备好
            if queues[0].state == "Waiting":
                queues[0].state = "Ready"
        else:
            break


if __name__ == "__main__":
    main()
