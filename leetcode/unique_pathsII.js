/** Follow up for "Unique Paths":
 * Now consider if some obstacles are added to the grids. How many unique paths 
 * would there be?
 * An obstacle and empty space is marked as 1 and 0 respectively in the grid.
 * Time Complexity: O(mn)
 * Space Complexity: O(1)
 */

/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    for (i = 0; i < obstacleGrid.length; ++i) {
        for (j = 0; j < obstacleGrid[i].length; ++j) {
            if (obstacleGrid[i][j] == 1)
                obstacleGrid[i][j] = 0
            else if (i == 0 && j == 0)
                obstacleGrid[i][j] = 1
            else if (i == 0)
                obstacleGrid[i][j] = obstacleGrid[i][j - 1]
            else if (j == 0)
                obstacleGrid[i][j] = obstacleGrid[i - 1][j]
            else
                obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                                   + obstacleGrid[i][j - 1]
        }
    }   
    return obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1]
};
