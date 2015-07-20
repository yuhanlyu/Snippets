# Given a 2d grid map of '1's (land) and '0's (water), count the number of 
# islands. An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all four edges of 
# the grid are all surrounded by water.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        def helper(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]) \
                and grid[row][col] == '1':
                grid[row][col] = '0'
                map(helper, (row + 1, row - 1,     row,     row),
                            (    col,     col, col + 1, col - 1))
                return 1
            return 0
        return sum(helper(row, col) for row in xrange(len(grid))
                                    for col in xrange(len(grid[row])))

if __name__ == "__main__":
    solution = Solution()
    print solution.numIslands([list("11110"), 
                               list("11010"),
                               list("11000"),
                               list("00000")])
    print solution.numIslands([list("11000"), 
                               list("11000"),
                               list("00100"),
                               list("00011")])
