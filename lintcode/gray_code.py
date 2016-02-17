class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        return [(x >> 1) ^ x for x in xrange(2 ** n)]
