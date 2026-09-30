class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                if len(stack) >= 2:
                    a, b = stack.pop(), stack.pop()
                    if c == '+':
                        stack.append(int(a) + int(b))
                    elif c == '-':
                        stack.append(int(b) - int(a))
                    elif c == '*':
                        stack.append(int(a) * int(b))
                    elif c == '/':
                        stack.append(int(float(b) / int(a)))

        return stack[0]

