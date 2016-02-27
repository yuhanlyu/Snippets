class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        DP = [0] * 101
        for i in xrange(1, len(A) + 1):
            old = DP[:]
            for j in xrange(101):
                DP[j] = min((old[k] + abs(A[i-1] - j) for k in 
                        xrange(max(0, j - target), min(target + j + 1, 101))))
        return min(DP)
