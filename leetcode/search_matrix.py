# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the 
# previous row.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
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

if __name__ == "__main__":
    solution = Solution()
    print solution.searchMatrix([[1], [3]], 3)
    print solution.searchMatrix([[1,   3,  5,  7],
                                 [10, 11, 16, 20],
                                 [23, 30, 34, 50]], 3)
