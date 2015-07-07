# Reverse digits of an integer.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x /= 10
        result *= sign
        return result if -2147483648 <= result <= 2147483647 else 0

if __name__ == "__main__":
    solution = Solution()
    print solution.reverse(-123)
