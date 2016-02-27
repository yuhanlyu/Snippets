class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        F = [0] * (len(B) + 1)
        for i in xrange(1, len(A) + 1):
            left_top, F[0] = F[0], 0
            for j in xrange(1, len(B) + 1):
                left_top, F[j] = F[j], 1 + left_top if A[i - 1] == B[j - 1] \
                                       else max(F[j], F[j - 1])
        return F[-1]
