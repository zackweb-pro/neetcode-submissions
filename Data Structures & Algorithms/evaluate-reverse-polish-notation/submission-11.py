from math import floor, ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = []
        for n in tokens:
            print(op)
            if n == '-':
                op.append(op.pop(-2)-op.pop(-1))
            elif n == '+':
                op.append(op.pop(-2)+op.pop(-1))
            elif n == '*':
                op.append(op.pop(-2)*op.pop(-1))
            elif n == '/':
                result = op.pop(-2)/op.pop(-1)
                op.append( ceil(result) if result < 0 else floor(result))
            else:
                op.append(int(n))
        print(op)
        return op[0]