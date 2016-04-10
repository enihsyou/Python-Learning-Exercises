from collections import defaultdict


def make_map(data):
    # defaultdict(<class 'list'>,
    # {(1, 2): [(1, 5), (7, 2), (7, 5)],
    # (1, 5): [(1, 2), (4, 7), (7, 5), (7, 2)],
    # (4, 7): [(1, 5), (7, 5)],
    # (7, 5): [(1, 2), (7, 2), (4, 7), (1, 5)],
    # (7, 2): [(1, 2), (7, 5), (1, 5)]})
    maps = defaultdict(list)
    for item in data:
        first, second = item[:2], item[2:]
        maps[first].append(second)
        maps[second].append(first)
    return maps


def possible(item, maps, used, length):
    possible_ways = maps[item]
    change = False
    for sub in possible_ways:
        if not ((item, sub) in used or (sub, item) in used):
            used.append((item, sub))
            change = possible(sub, maps, used, length)
            if change:
                return True
            elif len(used) == length:
                print('!!!')
                print(used)

                return used
            elif not used:
                continue
            else:
                used.pop()
                continue
    return change


def draw(data):
    maps = make_map(data)
    length = len(data)
    result = []
    for item in maps.keys():
        used = []
        possible(item, maps, used, length)
        # print(used)
        if used:
            result.append([a[0] for a in used] + [used[-1][-1]])
        # print(result)
        print()
    # result = set(result)
    print('------------')
    for item in result:
        print(item)
    print('------------')
    m = []
    if result:
        m = max(result, key = lambda x: len(x))
    print(tuple(m))
    return tuple(m)
    # if len(m) == len(data) + 1:
    #     print(tuple(m))
    #     return tuple(m)
    # else:
    #     print([])
    #     return []


draw({(1, 1, 2, 2), (2, 1, 2, 2), (2, 1, 3, 2), (2, 1, 3, 1), (1, 1, 0, 2), (1, 1, 0, 0), (3, 2, 3, 1),
      (0, 0, 0, 2)})
draw({(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)})
draw({(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)})
draw({(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)})


def checker(func, in_data, is_possible = True):
    user_result = func(in_data)
    if not is_possible:
        if user_result:
            print("How did you draw this?")
            return False
        else:
            return True
    if len(user_result) < 2:
        print("More points please.")
        return False
    data = list(in_data)
    for i in range(len(user_result) - 1):
        f, s = user_result[i], user_result[i + 1]
        if (f + s) in data:
            data.remove(f + s)
        elif (s + f) in data:
            data.remove(s + f)
        else:
            print("The wrong segment {}.".format(f + s))
            return False
    if data:
        print("You forgot about {}.".format(data[0]))
        return False
    return True


assert checker(draw,
               {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
assert checker(draw,
               {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
               False), "Example 2"
assert checker(draw,
               {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
