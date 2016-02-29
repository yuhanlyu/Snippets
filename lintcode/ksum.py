class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        DP = [[0 for _ in xrange(target + 1)] for _ in xrange(len(A) + 1)]
        DP[0][0] = 1
        for i in xrange(1, len(A) + 1):
            for t in xrange(target, 0, -1):
                for j in xrange(1, k + 1):
                    if t - A[i - 1] >= 0:
                        DP[j][t] += DP[j - 1][t - A[i - 1]]
        return DP[k][target]

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        cache = {}
        def helper(start, need, level):
            if level == k:
                return 1 if need == 0 else 0
            if (start, need, level) in cache:
                return cache[(start, need, level)]
            result = 0
            for i in xrange(start, len(A)):
                if need / (k - level) >= A[i]:
                    result += helper(i + 1, need - A[i], level + 1)
            cache[(start, need, level)] = result
            return result
        A.sort()
        return helper(0, target, 0)
