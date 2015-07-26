# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.
# Time Complexity: O(4^n)
# Space Complexity: O(4^n)

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        cur, result, x, y = ["("] * (n + 1) + [")"] * n, [], n, n
        while True:
            result.append(''.join(cur[1:]))
            if x >= 2 * n - 1: break
            cur[x], cur[y], x, y = ")", "(", x + 1, y + 1
            if cur[x] == ")":
                if x == 2 * y - 2: x += 1
                else: cur[x], cur[2], x, y = "(", ")", 3, 2
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.generateParenthesis(3)
