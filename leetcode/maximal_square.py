# Given a 2D binary matrix filled with 0's and 1's, find the largest square 
# containing all 1's and return its area.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        result = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i and j and matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i][j-1],  \
                                           matrix[i-1][j])
                result = max(result, matrix[i][j])
        return result * result

if __name__ == "__main__":
    solution = Solution()
    print solution.maximalSquare([list("1111"), list("1111"), list("1111")])
