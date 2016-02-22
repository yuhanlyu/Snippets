class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        F = [0] * (len(T) + 1)
        F[0] = 1
        for i in xrange(1, len(S) + 1):
            for j in xrange(min(i, len(T)), 0, -1):
                F[j] += F[j - 1] if T[j - 1] == S[i - 1] else 0
        return F[-1]
