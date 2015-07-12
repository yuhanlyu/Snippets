# Implement pow(x, n).
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
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

if __name__ == "__main__":
    solution = Solution()
    print solution.myPow(2, 10)
