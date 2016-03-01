class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
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
