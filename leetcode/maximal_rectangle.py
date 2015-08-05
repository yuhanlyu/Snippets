# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
# containing all ones and return its area.
# Time Complexity: O(mn)
# Space Complexity: O(1)

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        def largestRectangleArea(height):
            stack, result = [], 0
            height.append(0)
            for i, h in enumerate(height):
                while stack and h < height[stack[-1]]:
                    start = stack[-2] if len(stack) > 1 else -1
                    result = max(result, height[stack.pop()] * (i - start - 1))
                stack.append(i)
            return result
        if not matrix: return 0
        for i in xrange(0, len(matrix)):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i and matrix[i][j] == 1: matrix[i][j] += matrix[i - 1][j]
        return max((largestRectangleArea(row) for row in matrix))

if __name__ == "__main__":
    solution = Solution()
    print solution.maximalRectangle([list("0010"), list("0110")])
