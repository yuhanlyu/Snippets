class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        result = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i and j and matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i][j-1],  \
                                           matrix[i-1][j])
                result = max(result, matrix[i][j])
        return result * result
