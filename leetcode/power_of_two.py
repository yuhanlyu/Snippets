# Given an integer, write a function to determine if it is a power of two.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n & (n-1) == 0 and n > 0
                

if __name__ == "__main__":
    solution = Solution()
    print solution.isPowerOfTwo(1)
