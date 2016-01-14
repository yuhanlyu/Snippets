class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0:
            if A[m] >= B[n]:
                A[m + n + 1] = A[m]
                m -= 1
            else:
                A[m + n + 1] = B[n]
                n -= 1
        if n >= 0:
            A[:n + 1] = B[:n + 1]
