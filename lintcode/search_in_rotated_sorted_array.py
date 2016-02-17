class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] == target: return mid
            if (A[mid] <= A[right] and A[mid] < target <= A[right])\
            or (A[mid] > A[right] and
            not A[left] <= target < A[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return -1
