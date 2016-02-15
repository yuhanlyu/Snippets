class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        result = [1] + [0] * (len(A) - 1)
        for index in xrange(1, len(A)):
            result[index] = A[index - 1] * result[index - 1]
        product = 1
        for index in xrange(len(A) - 1, -1, -1):
            result[index] *= product
            product *= A[index]
        return result
