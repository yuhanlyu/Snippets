class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        if not matrix: return []
        for i, j in ((a, b) for a in xrange(len(matrix[0])/2)
                            for b in xrange(len(matrix[0]) - len(matrix[0])/2)):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
            matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
