class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        m, n, result = m + n - 2, min(m - 1, n - 1), 1
        for d in xrange(1, n + 1):
            result, m = (result * m) / d, m - 1
        return result
