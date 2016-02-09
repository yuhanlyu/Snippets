class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
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
