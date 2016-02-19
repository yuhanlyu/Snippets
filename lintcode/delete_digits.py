class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        A = list(A)
        for i in xrange(k):
            for j in xrange(len(A)):
                if j == len(A) - 1 or A[j + 1] < A[j]:
                    del A[j]
                    break
        return str(int(''.join(A)))
