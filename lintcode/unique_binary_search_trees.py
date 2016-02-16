class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        C = 1
        for i in xrange(1, n):
            C = (C * (4 * i + 2)) / (i + 2)
        return C
