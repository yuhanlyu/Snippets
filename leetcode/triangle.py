# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

if __name__ == "__main__":
    solution = Solution()
    print solution.minimumTotal([ [2], [3,4], [6,5,7], [4,1,8,3] ])
