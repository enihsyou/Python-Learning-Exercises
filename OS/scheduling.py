# -*- coding: utf-8 -*-
from itertools import cycle, islice


class QueueObject:
    current_time = 0

    def __init__(self, rounds=0, name="name",
                 default_priority=50, arrive_time=0, elapsed=0, remain=0,
                 count=0,
                 state="Waiting"):
        self.name = name  # 名字
        self.arrive_time = arrive_time  # 到来时间
        self.elapsed = elapsed  # 在CPU上已经运行的时间
        self.remain = remain  # 剩余要执行的CPU时间
        self.count = count  # 被执行次数
        self.round = rounds  # 时间片大小
        self.state = state  # 当前状态
        self.priority = default_priority - self.remain  # 优先级, 50 - 服务时间
        self.total = 0  # 总计时间

    def __str__(self):
        return "{o.name:<8}{o.priority:<8}{o.elapsed:<8}{o.remain:<8}" \
               "{o.count:<8}{o.round:<8}{o.state:<8}".format(o=self)

    def set_priority(self, priority):
        self.priority -= priority

    @classmethod
    def step(cls, instance=None, time=None):
        cls.current_time += time if time is not None else 1
        if instance:
            instance.set_priority(3)


class QueueHeader(QueueObject):
    """表头"""

    def __init__(self):
        super(QueueHeader, self).__init__()
        self.name = "Name"
        self.elapsed = "Elapsed"
        self.remain = "Remain"
        self.count = "Count"
        self.round = "Round"
        self.state = "State"
        self.priority = "Priority"


def input_name_and_service_time(round_times):
    queue = []
    input_string = input(
        "Please input name and service time with priority (if needed)\n"
        "type 'over' to stop:\n")
    while "over" != input_string:
        try:
            body = QueueObject(round_times)
            get = input_string.split()
            if 3 >= len(get) >= 2:
                body.name = get[0]  # 设置名字
                body.remain = int(get[1])  # 设置预计执行时间
                if len(get) == 3:
                    body.priority == int(get[2])
            else:  # 如果输入格式不对
                raise TypeError

            queue.append(body)  # 添加
            input_string = input()  # 下一个输入
        except TypeError:
            input_string = input(
                "Please try again, string and integer, split by a single space:\n")
        except ValueError:
            input_string = input(
                "Please try again, number needs to be an integer:\n")
    queue[0].state = "Running"
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
        print(item)


def sort_queue(queues: list, use_priority=False):
    ready, finished, un_finished = [], [], []
    for item in queues:
        if item.state == "Finished":
            finished.append(item)
        else:
            un_finished.append(item)
            if item.state == "Waiting":
                ready.append(item)
    # 排序队列
    queues.clear()
    queues.extend(un_finished)
    if use_priority:
        queues.sort(key=lambda x: x.priority, reverse=True)
        ready.sort(key=lambda x: x.priority, reverse=True)
    queues.extend(finished)

    return ready, finished, un_finished


def print_queue(ready, finished):
    if ready:
        print("Ready queue: " + ", ".join(map(lambda x: x.name, ready)))
    if finished:
        print("Finished queue: " + ", ".join(map(lambda x: x.name, finished)))


def perform_round_robin_next(queues, round_times, *args):
    this = queues[0]  # type: QueueObject
    assert this.state == "Running"
    this.count += 1
    if this.remain > round_times:  # 如果分片时间小于当前需求
        this.step(this, round_times)  # 增加总计执行时间
        this.remain -= round_times  # 相当于进行计算
        this.elapsed += round_times  # 递增执行时间
        this.state = "Waiting"
    else:
        this.step(this, this.remain)  # 增加总计执行时间
        this.elapsed += this.remain  # 递增执行时间
        this.remain = 0  # 如果分片时间够用，计算完成
        this.state = "Finished"  # 标记完成
        this.total = this.current_time - this.arrive_time


def perform_priority_preemptive_next(queues, *args):
    this = queues[0]  # type: QueueObject
    next = queues[1]
    assert this.state == "Running"
    # 如果分片时间小于当前需求
    while this.priority >= next.priority and this.remain != 0:
        this.remain -= 1  # 相当于进行一步计算
        this.elapsed += 1  # 递增执行时间
        this.count += 1  # 记录 进行了一步计算
        this.step(this)  # 增加总计执行时间
        this.state = "Waiting"
    else:
        this.state = "Finished"  # 标记完成
        this.total = this.current_time - this.arrive_time


def choose_function():
    func = perform_round_robin_next
    use_priority = False

    choice = 0
    while not choice:
        try:
            choice = int(input("1. Round-robin Algorithm\n"
                               "2. Priority Preemptive Scheduling Algorithm\n"))
        except ValueError:
            choice = 0

        if choice == 1 or choice == 2:
            break
        else:
            choice = 0
    if choice == 1:
        func = perform_round_robin_next
        use_priority = False
        print("{:-^80}".format("Round-robin Algorithm"))
    if choice == 2:
        func = perform_priority_preemptive_next
        use_priority = True
        print(
            "{:-^80}".format("Priority Preemptive Scheduling Algorithm"))

    return func, use_priority


def main():
    # 选择函数
    func, use_priority = choose_function()
    # 输入时间片大小
    round_times = input_round()
    # round_times = 2
    # 输入列表项目
    queues = input_name_and_service_time(round_times)
    # queues = [
    #     QueueObject(round_times, "a1", remain=3),
    #     QueueObject(round_times, "a2", remain=2),
    #     QueueObject(round_times, "a3", remain=4),
    #     QueueObject(round_times, "a4", remain=2),
    #     QueueObject(round_times, "a5", remain=1),
    # ]

    # 如果所有对象都没有完成，就继续循环
    break_flag = False
    while not break_flag:
        # 排序
        ready, finished, un_finished = sort_queue(queues, use_priority)
        # 设置第一个准备好
        if queues[0].state == "Waiting":
            queues[0].state = "Running"
        # 输出当前状态
        print_format(queues)
        # 输出队列
        print_queue(ready, finished)
        print()
        if not all(item.state == "Finished" for item in queues):
            func(queues, round_times)
            queues = list(islice(cycle(queues), 1, len(queues) + 1))  # 轮转列表
            # 设置第一个准备好
            if queues[0].state == "Waiting":
                queues[0].state = "Running"
        else:
            break_flag = True


if __name__ == "__main__":
    main()
