# Given a matrix of m x n elements (m rows, n columns), return all elements of 
# the matrix in spiral order.
# Time Complexity: O(mn)
# Space Complexity: O(mn)

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        remain = [len(matrix[0]), len(matrix) - 1]
        row, column, dir, result = 0, -1, 0, []
        while remain[dir % 2] > 0:
            result += (matrix[row + i * d[dir][0]][column + i * d[dir][1]] 
                       for i in xrange(1, remain[dir % 2] + 1))
            row += d[dir][0] * remain[dir % 2]
            column += d[dir][1] * remain[dir % 2]
            remain[dir % 2] -= 1
            dir = (dir + 1) % 4
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print solution.spiralOrder([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9],
                                [10, 11, 12]])
