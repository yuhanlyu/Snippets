class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        n, nn = 1, 3
        while abs(n - nn) > 1:
            n, nn = (n + x/n) / 2, n
        return n if n * n <= x else n - 1

if __name__ == "__main__":
    solution = Solution()
    print solution.sqrt(24)
