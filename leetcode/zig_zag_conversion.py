# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        result = [[] for _ in xrange(numRows)]
        step, index = 1, 0
        for c in s:
            result[index].append(c)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            if numRows > 1:
                index += step
        return ''.join([''.join(x) for x in result])

if __name__ == "__main__":
    solution = Solution()
    print solution.convert("PAYPALISHIRING", 3)
