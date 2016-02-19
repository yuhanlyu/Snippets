class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        i = m = 0
        while i < len(A) and i <= m:
            m = max(m, i + A[i])
            i += 1
        return i == len(A)
