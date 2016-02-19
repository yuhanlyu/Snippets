class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        m, next, jump = 0, 0, 0
        for i in xrange(len(A) - 1):
            next = max(next, i + A[i])
            if i == m:
                jump, m = jump + 1, next
        return jump
