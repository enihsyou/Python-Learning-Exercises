def cowsay(says):
    # Multiple spaces in a row are replaced by one space.
    say = says.split()

    line = []
    con_line_sum = 0  # 当前行的字数
    con_line = []  # 当前行的字符
    while say:  # 持续循环 只要还有
        pops = say.pop(0)
        con_line_sum += len(pops)
        con_line.append(pops)
        if con_line_sum < 39:  # 还有空间 添加空格
            con_line_sum += 1
            continue

        elif con_line_sum == 39:
            line.append(" ".join(con_line))
            con_line_sum = 0
            con_line = []

        else:  # 超过39 不要最后一个
            con_pop = con_line.pop()
            if len(con_pop) <= 39:
                say.insert(0, con_pop)
                line.append(" ".join(con_line))
            else:
                line.append(con_pop[:39])
                say.append(con_pop[39:])
            con_line_sum = 0
            con_line = []
    if con_line:
        line.append(" ".join(con_line))

    # now we have each line
    result_line = []

    # top and bottom
    max_len = len(max(line, key = lambda x: len(x)))

    top = "_" * (max_len + 2)
    bottom = "-" * (max_len + 2)

    if len(line) == 1:
        result_line.append("< " + " ".join(line) + " >")
    else:
        for each in range(len(line)):
            if each == 0:
                result_line.append("/ " + line[each].ljust(max_len) + " \\")
            elif each == len(line) - 1:
                result_line.append("\\ " + line[each].ljust(max_len) + " /")
            else:
                result_line.append("| " + line[each].ljust(max_len) + " |")
    # print(line)
    said = "\n".join(result_line)
    # print(said)
    print(r'''
 {top}
{said}
 {bottom}
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''.format(said = said, top = top, bottom = bottom))


cowsay("looooooooooooooooooooooooooooooooooooooooooooooong")
cowsay("loooooooooooooooooooooooooooooooooooong")
cowsay("spaces                           inside")
cowsay('Checkio rulezz')
cowsay('A longtextwithonlyonespacetofittwolines.')
cowsay(
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
