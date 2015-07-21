# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.
# Time Complexity: O(4^n)
# Space Complexity: O(4^n)

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        result = [[""]]
        for i in xrange(1, n + 1):
            result.append(["(" + p + ")" + q for j in xrange(i)
                           for p in result[j] for q in result[i - j - 1]])
        return result[n]

if __name__ == "__main__":
    solution = Solution()
    print solution.generateParenthesis(3)
