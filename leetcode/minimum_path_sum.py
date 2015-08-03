# Given a m x n grid filled with non-negative numbers, find a path from top 
# left to bottom right which minimizes the sum of all numbers along its path.
# Time Complexity: O(mn)
# Space Complexity: O(1)

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if i > 0 and j > 0: 
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]
        return grid[-1][-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.minPathSum([ [0,0,0], [0,1,0], [0,0,0] ])
