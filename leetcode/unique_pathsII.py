# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths 
# would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Time Complexity: O(mn)
# Space Complexity: O(1)

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        for i in xrange(len(obstacleGrid)):
            for j in xrange(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1: obstacleGrid[i][j] = 0
                elif i == 0 and j == 0: obstacleGrid[i][j] = 1
                elif i == 0: obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0: obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else: obstacleGrid[i][j] = obstacleGrid[i - 1][j]  \
                                         + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.uniquePathsWithObstacles([ [0,0,0], [0,1,0], [0,0,0] ])
