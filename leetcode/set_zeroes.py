# Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        zero_in_first_column = False
        for i in xrange(len(matrix)):
            if matrix[i][0] == 0: zero_in_first_column = True
            for j in xrange(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in xrange(len(matrix) - 1, -1, -1):
            for j in xrange(len(matrix[0]) - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if zero_in_first_column: matrix[i][0] = 0

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3],
              [1, 0, 1], 
              [1, 2, 3]]
    solution.setZeroes(matrix)
    print matrix
