def cowsay(says):
    # Multiple spaces in a row are replaced by one space.
    say = says.split()

    # If line is less than 40 characters, it will fit into one string. The string is quoted in <>.
    if len(says) < 40:
        # top and bottom
        said = "< " + " ".join(say) + " >"
        top = "_" * (len(said) - 2)
        bottom = "-" * (len(said) - 2)
    else:
        # top and bottom
        top = "_" * 41
        bottom = "-" * 41

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
                say.insert(0, con_line.pop())
                line.append(" ".join(con_line))
                con_line_sum = 0
                con_line = []
        if con_line:
            line.append(" ".join(con_line))

        # now we have each line
        result_line = []
        for each in range(len(line)):
            if each == 0:
                result_line.append("/ " + line[each].ljust(39) + " \\")
            elif each == len(line) - 1:
                result_line.append("\\ " + line[each].ljust(39) + " /")
            else:
                result_line.append("| " + line[each].ljust(39) + " |")
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


cowsay("spaces                           inside")
cowsay('Checkio rulezz')
cowsay('A longtextwithonlyonespacetofittwolines.')
cowsay(
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
