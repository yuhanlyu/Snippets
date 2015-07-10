# Given a positive integer, 
# return its corresponding column title as appear in an Excel sheet.
# Time Complexity: O(n)
# Space Complexity: O(lg n), the length of the result

class Solution:
     # @param {integer} n
     # @return {string}
     def convertToTitle(self, n):
        result = []
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            result.append(chr(ord('A') + remainder))
        result.reverse()
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    print solution.convertToTitle(26)
