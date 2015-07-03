# Given numRows, generate the first numRows of Pascal's triangle.
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if not numRows:
            return []
        pascal = [[1] * (i + 1) for i in xrange(numRows)]
        for row in xrange(numRows - 1):
            for index in xrange(1, row + 1):
                pascal[row+1][index] = pascal[row][index-1] + pascal[row][index]
        return pascal

if __name__ == "__main__":
    solution = Solution()
    print solution.generate(5)
