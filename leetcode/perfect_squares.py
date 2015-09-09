# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)
from math import sqrt, ceil

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for a in xrange(int(sqrt(n)) + 1):
            for b in xrange(a, int(sqrt(n - a * a)) + 1):
                c = int(sqrt(n - a * a - b * b))
                if a * a + b * b + c * c == n:
                    return sum(x > 0 for x in (a, b, c))
        return 4

if __name__ == "__main__":
    solution = Solution()
    print solution.numSquares(12)
    print solution.numSquares(13)
