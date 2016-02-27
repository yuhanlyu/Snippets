class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        F, result = [0] * (len(B) + 1), 0
        for i in xrange(1, len(A) + 1):
            left_top, F[0] = F[0], 0
            for j in xrange(1, len(B) + 1):
                left_top, F[j] = F[j], 1 + left_top if A[i - 1] == B[j - 1] \
                                       else 0
                if F[j] > result:
                    result = F[j]
        return result
