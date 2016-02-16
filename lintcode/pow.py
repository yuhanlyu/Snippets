class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        if n < 0:
            n, x = -n, 1.0 / x
        result = 1
        while n > 0:
            if n & 1:
                result *= x
            n /= 2
            x *= x
        return result
