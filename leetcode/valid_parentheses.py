# Given a string containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
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

if __name__ == "__main__":
    solution = Solution()
    print solution.isValid("()")
    print solution.isValid("()[]{}")
    print solution.isValid("(]")
    print solution.isValid("([)]")
