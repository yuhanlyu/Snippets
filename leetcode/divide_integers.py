# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
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

if __name__ == "__main__":
    solution = Solution()
    print solution.divide(100, 3)
    print solution.divide(1, -1)
