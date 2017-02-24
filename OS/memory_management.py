# -*- coding: utf-8 -*-
class Memory:
    """内存模拟"""

    def __init__(self, size):
        self.size = size - 1
        self.free = [Range(self.size)]

    def merge(self):
        if len(self.free) <= 1: return
        ordered = sorted(self.free, key=lambda x: x.start)
        # 整理结果数组
        result = ordered[:1]  # 初始 第一个元素
        last_number = result[0].stop  # 当前记录的数轴上最后一个位置
        for item in ordered[1:]:  # 对于剩下要处理的元素
            # 如果当前对象的左值和上一个对象的右值重叠
            if item.start <= last_number + 1:
                former = result.pop()  # 先踢出上一个
                new = Range(former.start, item.stop)  # 再构建一个新的范围
                result.append(new)  # 添加进去
            else:  # 如果是一个新范围
                result.append(item)
            last_number = item.stop

        self.free = result


class Range:
    def __init__(self, start, stop=None):
        if stop is not None:
            self.start = start
            self.stop = stop
        else:
            self.start = 0
            self.stop = start

    def __lt__(self, other):
        # 小在前 大在后
        assert self.stop >= self.start
        assert other.stop >= other.start
        # 不包含other
        assert not (
            self.start <= other.start and self.stop >= other.stop)
        # 不被other包含
        assert not (
            self.start >= other.start and self.stop <= other.stop)

        if self.start >= other.stop:
            return False
        if self.stop < other.start:
            return True

    def allocate(self, size):
        """分配空间"""
        assert self.stop - size + 1 >= self.start
        self.stop -= size

    def release(self, address, size):
        """释放空间"""
        self.stop, part = address, Range(address + size, self.stop)
        return part

    @property
    def size(self):
        return self.stop - self.start + 1

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.stop)


def perform_best_fit_algorithm(memory, action, *args):
    def _print_memory(memory):
        print_format(sorted(memory.free, key=lambda x: x.size))

    def assign(allocated, size):
        """给allocated数组内的Range 分配空间"""
        for space in allocated:
            if space.size >= size:  # 如果大小满足
                if space.size > size:
                    space.allocate(size)
                    memory.free = allocated
                elif space.size == size:
                    memory.free.remove(space)
                memory.merge()
                # 空间从小到大打印
                _print_memory(memory)
                print("Succeed")
                print("Address=%d\n" % (space.stop + 1))
                return True
        # 失败了
        _print_memory(memory)
        print("Failed")
        print("Too large size\n")
        return False

    def accept(memory, size, address):
        assert address + size <= memory.size
        may_be_new = Range(address, address + size - 1)  # 试图释放的分块
        # 如果没有和未分配的部分有交集
        if all(not set(range(may_be_new.start, may_be_new.stop)).intersection(
                range(space.start, space.stop))
                for space in memory.free):
            memory.free.append(may_be_new)
            memory.merge()
            _print_memory(memory)
            print("Succeed")
            return True
        _print_memory(memory)
        print("Failed")
        return False

    if action == "assign":
        # 一份数轴的按空间由小到大排序的引用
        assign(sorted(memory.free, key=lambda x: x.size), *args)
    elif action == "accept":
        accept(memory, *args)


def perform_first_fit_algorithm(memory, action, *args):
    def _print_memory(memory):
        print_format(sorted(memory.free, key=lambda x: x.start))

    def assign(allocated, size):
        """给allocated数组内的Range 分配空间"""
        for space in allocated:
            if space.size >= size:  # 如果大小满足
                if space.size > size:
                    space.allocate(size)
                    memory.free = allocated
                elif space.size == size:
                    memory.free.remove(space)
                memory.merge()
                # 空间按照起始地址打印
                _print_memory(memory)
                print("Succeed")
                print("Address=%d\n" % (space.stop + 1))
                return True
        # 失败了
        _print_memory(memory)
        print("Failed")
        print("Too large size\n")
        return False

    def accept(memory, size, address):
        assert address + size <= memory.size
        may_be_new = Range(address, address + size - 1)  # 试图释放的分块
        # 如果没有和未分配的部分有交集
        if all(not set(range(may_be_new.start, may_be_new.stop)).intersection(
                range(space.start, space.stop))
                for space in memory.free):
            memory.free.append(may_be_new)
            memory.merge()
            _print_memory(memory)
            print("Succeed")
            return True
        _print_memory(memory)
        print("Failed")
        return False

    if action == "assign":
        # 一份数轴的按起始地址由小到大排序的引用
        assign(sorted(memory.free, key=lambda x: x.start), *args)
    elif action == "accept":
        accept(memory, *args)


def input_memory_size():
    input_string = input("Please input memory size (B):\n")
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


def choose_function():
    while True:
        choice = input("1. Best-fit Algorithm\n"
                       "2. First-fit Algorithm\n")
        if choice == "1" or choice == "2":
            break
    if choice == "1":
        func = perform_best_fit_algorithm
        print("{:-^80}".format("Best-fit Algorithm"))
        return func

    if choice == "2":
        func = perform_first_fit_algorithm
        print(
            "{:-^80}".format("First-fit Algorithm"))
        return func


def choose_action(max_size):
    def _input_size():
        while True:
            try:
                size = int(input("Input size:\n"))
                assert max_size >= size > 0
            except (ValueError, AssertionError):
                pass
            else:
                return size

    def _input_address():
        while True:
            try:
                address = int(input("Input address:\n"))
                assert max_size >= address >= 0
            except (ValueError, AssertionError):
                pass
            else:
                return address

    while True:
        choice = input("1. Assign\n"
                       "2. Accept\n")
        if choice.lower().startswith("as"):
            choice = "1"
        elif choice.lower().startswith("ac"):
            choice = "2"
        if choice == "1" or choice == "2":
            break
    if choice == "1":
        func = "assign"
        size = _input_size()
        return func, (size,)
    if choice == "2":
        func = "accept"
        address = _input_address()
        size = _input_size()
        return func, (size, address)


def print_format(memory_space):
    print("{:<8s}{:<8s}{:<8s}{:<8s}".format("Index", "Start", "Stop", "Size"))
    if len(memory_space) < 1: return
    for i, item in enumerate(memory_space, 1):
        print("{:<8d}{o.start:<8}{o.stop:<8}{o.size:<8}".format(i, o=item))


def main():
    memory_size = input_memory_size()
    func = choose_function()
    # memory = Memory(memory_size)
    memory = Memory(32768)
    # memory.free = [Range(3000, 5766), Range(0, 2766), Range(6000, 7000)]
    print_format(memory.free)
    while True:
        action, args = choose_action(memory_size)
        func(memory, action, *args)


if __name__ == "__main__":
    main()
