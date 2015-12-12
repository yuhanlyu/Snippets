# Given a 2D matrix matrix, find the sum of the elements inside the rectangle 
# defined by its upper left corner (row1, col1) and lower right corner 
# (row2, col2).
# Time Complexity: O(1)
# Space Complexity: O(n^2)

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [ [0] * (m + 1) for i in xrange(n + 1) ]
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                self.sums[i][j] = matrix[i - 1][j - 1] + self.sums[i][j - 1] \
                                + self.sums[i - 1][j] - self.sums[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] \
             - self.sums[row1][col2 + 1] + self.sums[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
