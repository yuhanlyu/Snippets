class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = [[0] * n for _ in xrange(n)]
        row, column, dir = 0, 0, 0
        for i in xrange(1, n * n + 1):
            result[row][column] = i
            nr, nc = row + d[dir][0], column + d[dir][1]
            if 0 <= nr < n and 0 <= nc < n and result[nr][nc] == 0:
                row, column = nr, nc
            else:
                dir = (dir + 1) % 4
                row, column = row + d[dir][0], column + d[dir][1]
        return result
