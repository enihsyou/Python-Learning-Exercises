def checkio(expression):
    stack = []
    bracketss = {')': '(', ']': '[', '}': '{'}
    fbrackets = ['(', '[', '{']
    bbrackets = [')', ']', '}']
    for char in expression:
        if char in fbrackets:
            stack.append(char)
        elif char in bbrackets:
            if stack and bracketss[char] == stack[-1]:
                stack.pop()
            else:
                return False

    return True if not stack else False
ord()

checkio("(((1+(1+1))))]")
# checkio("(((([[[{{{3}}}]]]]))))")

assert checkio("((5+3)*2+1)") == True, "Simple"
assert checkio("{[(3+1)+2]+}") == True, "Different types"
assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
assert checkio("2+3") == True, "No brackets, no problem"
