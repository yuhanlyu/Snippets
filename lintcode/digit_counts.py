class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        result = 0
        for i in xrange(n + 1):
            for c in str(i):
                if int(c) == k:
                    result += 1
        return result
