class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        negatives = 0
        for i in xrange(len(A)):
            if A[i] < 0:
                A[i], A[negatives] = A[negatives], A[i]
                negatives += 1
        if negatives == len(A) - negatives:
            left = 1;
            right = len(A) - 2;
        elif negatives > len(A) - negatives:
            left = 1;
            right = len(A) - 1;
        else:
            left = 0;
            right = len(A) - 2;
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2
