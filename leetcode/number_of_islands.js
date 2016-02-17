/* Given a 2d grid map of '1's (land) and '0's (water), count the number of 
 * islands. An island is surrounded by water and is formed by connecting 
 * adjacent lands horizontally or vertically. You may assume all four edges of 
 * the grid are all surrounded by water.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    function helper(row, col) {
        if (0 <= row && row < grid.length
         && 0 <= col && grid[row].length
         && grid[row][col] === '1') {
            grid[row][col] = '0'
            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)
            return 1
        }
        return 0
    }
    for (var result = 0, i = 0; i < grid.length; ++i)
        for (var j = 0; j < grid[i].length; ++j)
            result += helper(i, j)
    return result
};
