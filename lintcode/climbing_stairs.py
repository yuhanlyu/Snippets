class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        x, y, a, b = 1, 0, 1, 1
        while n > 0:
            if n & 1: x, y = a * x + b * y, b * x + y * (a - b)
            a, b, n = a * a + b * b, b * (2 * a - b), n >> 1
        return x
