class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        if not A: return 0
        max, current = 0, 0
        for i in xrange(len(A) - 1):
            if A[i] > A[i + 1]:
                current += 1
                if current > max:
                    max = current
            else:
                current = 0
        current = 0    
        for i in xrange(len(A) - 1, 0, -1):
            if A[i] > A[i - 1]:
                current += 1
                if current > max:
                    max = current
            else:
                current = 0
        return max + 1
