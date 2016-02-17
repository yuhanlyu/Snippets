class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        def bsearch(A, target):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if A[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        lower = bsearch(A, target)
        if lower == len(A) or A[lower] != target: return [-1, -1]
        return [lower, bsearch(A, target + 1) - 1]
