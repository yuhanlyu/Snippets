class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] == target: return True
            if A[left] == A[mid] == A[right]:
                left += 1
                right -= 1
            elif (A[left] <= target < A[mid]) or (A[left] > A[mid]
                  and not (A[mid] < target <= A[right])):
                right = mid - 1
            else:
                left = mid + 1
        return False
