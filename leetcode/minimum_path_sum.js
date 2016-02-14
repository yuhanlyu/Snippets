/* Given a m x n grid filled with non-negative numbers, find a path from top 
 * left to bottom right which minimizes the sum of all numbers along its path.
 * Time Complexity: O(mn)
 * Space Complexity: O(1)
 */
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    for (var i = 0; i < grid.length; ++i) {
        for (var j = 0; j < grid[i].length; ++j) {
            if (i > 0 && j > 0)
                grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1])
            else if (i > 0)
                grid[i][j] += grid[i - 1][j]
            else if (j > 0)
                grid[i][j] += grid[i][j - 1]
        }
    }
    return grid[grid.length - 1][grid[0].length - 1]
};
