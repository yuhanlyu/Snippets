# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. 
# Each operand may be an integer or another expression.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        oprs, ops = [], [lambda a, b: b + a, lambda a, b: b - a,
                         lambda a, b: b * a, lambda a, b: int(float(b) / a)]
        for token in tokens:
            if not token.isdigit() and len(token) == 1:
                oprs.append(ops['+-*/'.index(token)](oprs.pop(), oprs.pop()))
            else: 
                oprs.append(int(token))
        return oprs[0]

if __name__ == "__main__":
    solution = Solution()
    print solution.evalRPN(["2", "1", "+", "3", "*"])
    print solution.evalRPN(["4", "13", "5", "/", "+"])
