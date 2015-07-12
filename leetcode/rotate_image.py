# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        for i, j in ((a, b) for a in xrange(len(matrix[0])/2)
                            for b in xrange(len(matrix[0]) - len(matrix[0])/2)):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
            matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j] 

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    solution = Solution()
    solution.rotate(matrix)
    print matrix
