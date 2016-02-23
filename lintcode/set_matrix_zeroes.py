class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
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
