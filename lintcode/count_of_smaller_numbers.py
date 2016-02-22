class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        A.sort()
        result = []
        for q in queries:
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if A[mid] < q:
                    left = mid + 1
                else:
                    right = mid - 1
            result.append(left)
        return result
