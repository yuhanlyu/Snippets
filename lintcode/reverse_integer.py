class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        sign = 1 if n >= 0 else -1
        x = abs(n)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x /= 10
        result *= sign
        return result if -2147483648 <= result <= 2147483647 else 0
