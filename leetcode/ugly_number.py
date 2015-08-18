# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# For example, 6, 8 are ugly while 14 is not ugly since it includes another 
# prime factor 7.
# Note that 1 is typically treated as an ugly number.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num:
            for factor in (2, 3, 5):
                while num % factor == 0:
                    num /= factor
        return num == 1

if __name__ == "__main__":
    solution = Solution()
    print solution.isUgly(6)
    print solution.isUgly(8)
    print solution.isUgly(14)
