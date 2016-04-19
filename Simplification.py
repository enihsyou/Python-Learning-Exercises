import re
import collections

import math

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
            for i in range(len(min(self.power, other.power))):
                self.power[i] += other.power[i]
        return self.__repr__()

    def __sub__(self, other):
        if isinstance(other, int):
            self.power[0] -= other
        elif isinstance(other, X):
            for i in range(len(min(self.power, other.power))):
                self.power[i] -= other.power[i]
        return self.__repr__()

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

    def __radd__(self, other):
        self.__add__(other)

    def __rsub__(self, other):
        self.__sub__(other)

    def __rmul__(self, other):
        self.__mul__(other)

    def __repr__(self):
        string = ""
        for index, num in enumerate(self.power[::-1]):
            index = len(self.power) - index - 1

            if self.power == [0]:
                return '0'
            if num == 0:
                continue
            if index == 0:
                string += "{}".format(num)
                break
            else:
                part = "x"
                if num != 1:
                    part = "{}*".format(num) + part
                if index != 1:
                    part += "**{}".format(index)

                string += part

            string += '+'
        if string.endswith('+'):
            return string[:-1]
        return string


x = X()
while True:
    inp = input()
    print(eval(inp))


class ExpressionEvaluator:
    def __init__(self):
        self.tokens = None
        self.tok = None
        self.nexttok = None
        self.power = [0]
        self.stack = [[]]

    # Parser
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        print(self.expr())
        # return self.expr()

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
        if exprval == 'x':
            self.stack[-1].append('x')
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()

            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        """factor (*) factor"""
        termval = self.factor()
        if termval == 'x':
            self.stack[-1].append('x')
        while self._accept('TIMES'):
            op = self.tok.type
            right = self.factor()

            if op == 'TIMES':
                termval *= right
                # elif op == 'POWER':
                #     termval = math.pow(termval, right)
        return termval

    def factor(self):
        """NUM | ( expr )"""
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('X'):
            return self.tok.value
        elif self._accept('LPAREN'):
            self.stack.append([])
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def simplify(data):
    e = ExpressionEvaluator()
    print(e.parse(data))

# simplify("x+x*x+x*x*x") == "x**3+x**2+x"
# simplify("(x-1)*(x+1)") == "x**2-1"
# simplify("(x+1)*(x+1)") == "x**2+2*x+1"
# simplify("(x+3)*x*2-x*x") == "x**2+6*x"
# simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6"
# simplify("x*x-(x-1)*(x+1)-1") == "0"
# simplify("5-5-x") == "-x"
# simplify("x*x*x-x*x*x-1") == "-1"
