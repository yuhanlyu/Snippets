class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n, count = n / 5, count + n / 5
        return count

if __name__ == "__main__":
    solution = Solution()
    print solution.trailingZeroes(4617)
