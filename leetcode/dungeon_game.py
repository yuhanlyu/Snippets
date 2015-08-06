# The demons had captured the princess (P) and imprisoned her in the 
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid 
# out in a 2D grid. Our valiant knight (K) was initially positioned in the 
# top-left room and must fight his way through the dungeon to rescue the 
# princess.
# The knight has an initial health point represented by a positive integer. 
# If at any point his health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or 
# contain magic orbs that increase the knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight decides to 
# move only rightward or downward in each step.
# Write a function to determine the knight's minimum initial health so that he 
# is able to rescue the princess.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        F = [2 ** 32] * (len(dungeon[-1]) + 1)
        F[-2] = 1
        for i in xrange(len(dungeon) - 1, -1, -1):
            for j in xrange(len(dungeon[i]) - 1, -1, -1):
                F[j] = max(1, min(F[j], F[j + 1]) - dungeon[i][j])
        return F[0]

if __name__ == "__main__":
    solution = Solution()
    print solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
