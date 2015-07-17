# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / 
# operators and empty spaces . The integer division should truncate toward zero.
# You may assume that the given expression is always valid.
# Time Complexity: O(n)
# Space Complexity: O(1), assuming atoi in-place

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        result, val, op, index = 0, 0, '+', 0
        ariths = [lambda a, b: a + b, lambda a, b: a - b,
                  lambda a, b: a * b, lambda a, b: int(float(a) / b)]
        while index < len(s):
            if s[index].isdigit():
                begin = index
                while index + 1 < len(s) and s[index + 1].isdigit():
                    index += 1
                val = ariths['+-*/'.find(op)](val, int(s[begin:index + 1]))
            elif s[index] != ' ':
                if s[index] in '+-':
                   result, val = result + val, 0
                op = s[index]
            index += 1
        return result + val

if __name__ == "__main__":
    solution = Solution()
    print solution.calculate("3+2*2")
    print solution.calculate(" 3/2 ")
    print solution.calculate(" 3+5 / 2 ")
    print solution.calculate("1*2-3/4+5*6-7*8+9/10")
