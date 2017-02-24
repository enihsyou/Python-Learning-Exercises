def letter_queue(data):
    fu = []
    for func in data:
        fu.append(func.split())
    dic = {"PUSH": lambda x, y: x.append(y),
           "POP" : lambda x, y: x.pop(y)}
    queue = []
    for item in fu:
        if len(item) == 2:
            dic[item[0]](queue, item[1])
        elif queue:
            dic[item[0]](queue, 0)
        else:
            continue
    return "".join(queue)


letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])
letter_queue(["POP", "POP"])
letter_queue(["PUSH H", "PUSH I"])
letter_queue([])
