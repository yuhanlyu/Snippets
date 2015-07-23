# Given a non-negative integer n representing the total number of bits in 
# the code, print the sequence of gray code. 
# A gray code sequence must begin with 0.
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        return [(x >> 1) ^ x for x in xrange(2 ** n)]

if __name__ == "__main__":
    solution = Solution()
    print solution.grayCode(2)
