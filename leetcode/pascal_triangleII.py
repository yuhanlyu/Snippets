# Given an index k, return the kth row of the Pascal's triangle.
# Time complexity: O(k^2) (without using multiplication/division)
# Space complexity: O(k) (use only one array)

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = [1] + [0] * (rowIndex)
        for row in xrange(rowIndex):
            for index in xrange(row, -1, -1):
                result[index + 1] += result[index]
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.getRow(3)
