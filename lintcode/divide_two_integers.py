class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        ans, tmp, shift, n, d = 0, abs(divisor), 0, abs(dividend), abs(divisor)
        while (tmp << 1) <= n:
            shift += 1
            tmp <<= 1
        while d <= n:
            if n >= tmp:
                n -= tmp
                ans |= (1 << shift)
            tmp >>= 1
            shift -= 1
        ans = ans if dividend * divisor >= 0 else -ans
        return ans if -2147483648 <= ans <= 2147483647 else 2147483647
