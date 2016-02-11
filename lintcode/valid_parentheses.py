class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ')':
                if stack.pop() != '(': return False
            elif c == ']':
                if stack.pop() != '[': return False
            else:
                if stack.pop() != '{': return False
        return not stack
