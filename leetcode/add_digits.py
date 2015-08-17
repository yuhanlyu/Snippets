# Given a non-negative integer num, repeatedly add all its digits until the 
# result has only one digit.
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return num - 9 * ((num - 1) / 9) if num else 0

if __name__ == "__main__":
    solution = Solution()
    print solution.addDigits(38)
