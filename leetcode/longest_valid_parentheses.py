# Given a string containing just the characters '(' and ')', find the length 
# of the longest valid (well-formed) parentheses substring.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        result, stack = 0, [-1]
        for i, c in enumerate(s):
            if stack[-1] != -1 and c == ')' and s[stack[-1]] == '(':
                stack.pop()
                result = max(result, i - stack[-1])
            else:
                stack.append(i)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.longestValidParentheses("()")
    print solution.longestValidParentheses("(()")
    print solution.longestValidParentheses(")()())")
