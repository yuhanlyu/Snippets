# Given an integer n, count the total number of digit 1 appearing in all 
# non-negative integers less than or equal to n.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        count, power = 0, 1
        while power <= n:
            count += ((n / power + 8) / 10) * power
            if (n / power) % 10 == 1: count += n % power + 1
            power *= 10
        return count

if __name__ == "__main__":
    solution = Solution()
    print solution.countDigitOne(13)
