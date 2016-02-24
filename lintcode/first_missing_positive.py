class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in xrange(len(A)):
            num = A[i] - 1
            while 0 <= num < len(A) and A[num] != num + 1:
                A[num], A[i], num = A[i], A[num], A[num] - 1
        for i, num in enumerate(A):
            if num != i + 1:
                return i + 1
        return len(A) + 1
