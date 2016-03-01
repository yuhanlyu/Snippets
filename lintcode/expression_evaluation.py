class Solution:
    # @param expression: a list of strings;
    # @return: an integer
    def evaluateExpression(self, expression):
        return self.evaRPN(self.convertToRPN(expression))
        
    def evaRPN(self, tokens):
        oprs, ops = [], [lambda a, b: b + a, lambda a, b: b - a,
                     lambda a, b: b * a, lambda a, b: int(float(b) / a)]
        for token in tokens:
            if not token.isdigit() and len(token) == 1:
                oprs.append(ops['+-*/'.index(token)](oprs.pop(), oprs.pop()))
            else:
                oprs.append(int(token))
        return oprs[0] if oprs else 0
    
    def convertToRPN(self, expression):
        precedence = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
        result, stack = [], []
        for token in expression:
            if token.isdigit():
                result.append(token)
            elif token == "(":
                stack.append("(")
            elif token == ")":
                while stack:
                    token = stack.pop()
                    if token == "(":
                        break
                    result.append(token)
            else:
                while stack and precedence[token] <= precedence[stack[-1]]:
                    result.append(stack.pop())
                stack.append(token)
        while stack:
            result.append(stack.pop())
        return result
