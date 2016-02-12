class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        result, n, m = [], len(matrix), len(matrix[0])
        for i in xrange(n + m - 1):
            step = -1 if i % 2 == 0 else 1
            begin = min(n - 1, i) if i % 2 == 0 else max(0, i - m + 1)
            end = max(-1, i - m) if i % 2 == 0 else min(n, i + 1)
            for j in xrange(begin, end, step):
                result.append(matrix[j][i - j])
        return result
