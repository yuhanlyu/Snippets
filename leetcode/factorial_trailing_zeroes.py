# Given an integer n, return the number of trailing zeroes in n!.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n /= 5
            count += n
        return count

if __name__ == "__main__":
    solution = Solution()
    print solution.trailingZeroes(4617)
