# Given numRows, generate the first numRows of Pascal's triangle.
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        pascal = []
        for i in xrange(numRows):
            row = [1] if pascal else []
            for j in xrange(len(pascal) - 1):
                row.append(pascal[-1][j] + pascal[-1][j+1])
            row.append(1) 
            pascal.append(row)
        return pascal

if __name__ == "__main__":
    solution = Solution()
    print solution.generate(5)
