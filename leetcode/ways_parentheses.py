# Given a string of numbers and operators, return all possible results from 
# computing all the different possible ways to group numbers and operators. 
# The valid operators are +, - and *.
# Time Complexity: O(4^n)
# Space Complexity: O(4^n)

import re, operator

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, 
                   '*': operator.mul}.get, tokens[1::2])
        F = [[[nums[i]] if j == i else [] for j in xrange(len(nums))] 
                                          for i in xrange(len(nums))]
        for l in xrange(1, len(nums)):
            for i in xrange(len(nums) - l):
                F[i][i+l].extend((ops[j](a, b) for j in xrange(i, i + l)
                              for a in F[i][j] for b in F[j+1][i+l]))
        return F[0][-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.diffWaysToCompute("2-1-1")
    print solution.diffWaysToCompute("2*3-4*5")
