# A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
# the diagram below).
# The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in 
# the diagram below).
# How many possible unique paths are there?
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        m, n, result = m + n - 2, min(m - 1, n - 1), 1 
        for d in xrange(1, n + 1):
            result, m = (result * m) / d, m - 1
        return result 

if __name__ == "__main__":
    solution = Solution()
    print solution.uniquePaths(5, 3)
