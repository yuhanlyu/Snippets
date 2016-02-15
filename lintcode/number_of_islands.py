class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        def helper(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]) \
                and grid[row][col] == 1:
                grid[row][col] = 0
                map(helper, (row + 1, row - 1,     row,     row),
                            (    col,     col, col + 1, col - 1))
                return 1
            return 0
        return sum(helper(row, col) for row in xrange(len(grid))
                                    for col in xrange(len(grid[row])))
