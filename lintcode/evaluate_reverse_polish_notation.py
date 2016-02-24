class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        oprs, ops = [], [lambda a, b: b + a, lambda a, b: b - a,
                         lambda a, b: b * a, lambda a, b: int(float(b) / a)]
        for token in tokens:
            if not token.isdigit() and len(token) == 1:
                oprs.append(ops['+-*/'.index(token)](oprs.pop(), oprs.pop()))
            else:
                oprs.append(int(token))
        return oprs[0]
