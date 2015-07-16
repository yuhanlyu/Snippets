# implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), 
# the plus + or minus sign -, non-negative integers and empty spaces .
# You may assume that the given expression is always valid.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        result, index, signs = 0, 0, [1, 1]
        while index < len(s):
            if s[index].isdigit():
                start = index
                while index + 1 < len(s) and s[index + 1].isdigit():
                    index += 1
                result += signs.pop() * int(s[start:index + 1])
            elif s[index] in '+-(':
                signs.append(signs[-1] if s[index] != '-' else -signs[-1])
            elif s[index] == ')':
                signs.pop()
            index += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.calculate("1 + 1")
    print solution.calculate(" 2-1 + 2 ")
    print solution.calculate("(1+(4+5+2)-3)+(6+8)")
