import re
import collections

X = r'(?P<X>x)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
# POWER = r'(?P<POWER>\*\*)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([X, NUM, PLUS, MINUS, TIMES, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


class X:
    def __init__(self):
        self.stack = []
        self.power = [0, 1]

    def __add__(self, other):
        if isinstance(other, int):
            self.power[0] += other
        elif isinstance(other, X):
            for i in range(len(other.power)):
                if i >= len(self.power): self.power.append(0)
                self.power[i] += other.power[i]
        # return self.__repr__()
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.power[0] -= other
        elif isinstance(other, X):
            for i in range(len(other.power)):
                if i >= len(self.power): self.power.append(0)
                self.power[i] -= other.power[i]
        # return self.__repr__()
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            self.power = list(map(lambda a: a * other, self.power))

        elif isinstance(other, X):
            power = self.power
            power2 = other.power
            self.power = [0]
            for i in range(len(power)):
                for j in range(len(power2)):
                    if i + j >= len(self.power):
                        self.power.extend([0] * (i + j - len(self.power) + 1))
                    self.power[i + j] += power[i] * power2[j]
        return self

    def __radd__(self, other):
        self.__add__(other)
        return self

    def __rsub__(self, other):
        self.power = [-x for x in self.power]
        if isinstance(other, int):
            self.power[0] += other
        elif isinstance(other, X):
            for i in range(len(other.power)):
                if i >= len(self.power): self.power.append(0)
                self.power[i] += other.power[i]
        # return self.__repr__()
        return self

    def __rmul__(self, other):
        self.__mul__(other)
        return self

    def __repr__(self):
        string = ""
        for index, num in enumerate(self.power[::-1]):
            index = len(self.power) - index - 1

            if set(self.power) == {0}:
                return '0'
            if num == 0:
                continue

            if index == 0:
                string += "{:+}".format(num)
                break
            else:
                part = "x"
                if num == 1:
                    part = '+' + part
                elif num == -1:
                    part = '-' + part
                else:
                    part = "{:+}*".format(num) + part

                if index != 1:
                    part += "**{}".format(index)
            string += part

        return string.strip('+')


# x = X()
# while True:
#     inp = input()
#     print(eval(inp))


class ExpressionEvaluator:
    def __init__(self):
        self.tokens = None
        self.tok = None
        self.nexttok = None

    # Parser
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        # print(self.expr())
        return str(self.expr())

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected', toktype)

    # Grammar rules
    def expr(self):
        """term (+|-) term"""
        exprval = self.term()
        # if exprval == 'x':
        #     self.stack[-1].append('x')
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()

            if op == 'PLUS':
                exprval += right
                # exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval -= right
                # exprval = ('-', exprval, right)
        return exprval

    def term(self):
        """factor (*) factor"""
        termval = self.factor()

        while self._accept('TIMES'):
            op = self.tok.type
            right = self.factor()

            if op == 'TIMES':
                termval *= right
                # termval = ('*', termval, right)
        return termval

    def factor(self):
        """NUM | ( expr )"""
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('X'):
            # return self.tok.value
            return X()
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def simplify(data):
    e = ExpressionEvaluator()
    print(data, e.parse(data))
    print(e.parse(data))
    return e.parse(data)


# while True:
#     inp = input()
#     simplify(inp)

simplify(u"(x+13-(x*x*x)*x-(x)-x+19-x*10*(x*62)+x-x*0*(66)*83-93+x-(21*x+(85-77+x-x)))")
if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"
