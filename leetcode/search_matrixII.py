# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [ [1,   4,  7, 11, 15],
               [2,   5,  8, 12, 19],
               [3,   6,  9, 16, 22],
               [10, 13, 14, 17, 24],
               [18, 21, 23, 26, 30] ]
    print solution.searchMatrix(matrix, 5)
    print solution.searchMatrix(matrix, 20)
