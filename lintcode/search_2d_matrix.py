class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left < len(matrix) and matrix[left][0] == target: return True
        if left == 0: return False
        index = left - 1
        left, right = 0, len(matrix[index]) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if matrix[index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left < len(matrix[index]) and matrix[index][left] == target
