# Given a column title as appear in an Excel sheet, 
# return its corresponding column number.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        result = 0
        for c in s:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.titleToNumber("AB")
