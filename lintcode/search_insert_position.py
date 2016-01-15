class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
