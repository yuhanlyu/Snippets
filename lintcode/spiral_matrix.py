class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        if not matrix: return []
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        remain = [len(matrix[0]), len(matrix) - 1]
        row, column, dir, result = 0, -1, 0, []
        while remain[dir % 2] > 0:
            result.extend((matrix[row + i * d[dir][0]][column + i * d[dir][1]]
                           for i in xrange(1, remain[dir % 2] + 1)))
            row += d[dir][0] * remain[dir % 2]
            column += d[dir][1] * remain[dir % 2]
            remain[dir % 2] -= 1
            dir = (dir + 1) % 4
        return result
