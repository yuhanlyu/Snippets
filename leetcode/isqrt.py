# Implement int sqrt(int x).  Compute and return the square root of x.
# Time Complexity: O(lg lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        n, nn = 1, 3
        while abs(n - nn) > 1:
            n, nn = (n + x/n) / 2, n
        return n if n * n <= x else n - 1

if __name__ == "__main__":
    solution = Solution()
    print solution.mySqrt(24)
