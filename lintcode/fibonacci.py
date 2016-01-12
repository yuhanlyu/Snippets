class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        first, second = 0, 1
        for _ in xrange(n - 1):
            first, second = second, first + second
        return first

if __name__ == "__main__":
    solution = Solution()
    print solution.fibonacci(10)
    print solution.fibonacci(1)
