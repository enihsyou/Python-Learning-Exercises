def add_number(data, res):
    if data:
        res += data.pop()

        resu = add_number(data, res)
        return resu
    else:
        return res


def checkio(data):
    result = 0
    return add_number(data, result)


checkio([2, 2, 2, 2, 2, 2])
