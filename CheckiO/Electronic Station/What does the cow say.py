def cowsay(says):
    # Multiple spaces in a row are replaced by one space.
    say = says.split()

    if says[0] == ' ': say[0] = ' ' + say[0]
    if says[-1] == ' ': say[-1] = say[-1] + ' '

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
            if con_pop[0] == ' ':
                line.append(' ')
                say.insert(0, con_pop[1:])
            elif len(con_pop) <= 39:
                say.insert(0, con_pop)
                line.append(" ".join(con_line))
            else:
                line.append(con_pop[:39])
                say.insert(0, con_pop[39:])
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
    return r'''
 {top}
{said}
 {bottom}
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''.format(said = said, top = top, bottom = bottom)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                               'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines

cowsay(" a")
cowsay("mooooooooooooooooooooooooooooooooooooooo mooo")

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

# def cowsay(s):
#     s, l = [''] * (s[0] == ' ') + s.split() + [''] * (s[-1] == ' '), []
#     while s:
#         x = ''
#         while s and len(x) + len(s[0]) < 40:
#             x, s = x + s[0] + ' ', s[1:]
#         if s and not x:
#             x, s[0] = x + s[0][:39] + ' ', s[0][39:]
#         l.append(x[:-1])
#     n, m = len(l), max(map(len, l))
#     f = n == 1 and ['< {} >'] or ['/ {} \\'] + ['| {} |'] * (n - 2) + ['\\ {} /']
#     return '\n ' + '_' * (m + 2) + '\n' + '\n'.join(f[i].format(l[i].ljust(m)) for i in range(n)) + '\n ' + '-' * (
#     m + 2) + COW

cowsay(" 0123456789012345678901234567890123456789 ")
