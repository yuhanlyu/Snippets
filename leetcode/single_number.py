# Given an array of integers, every element appears twice except for one. 
# Find that single one.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        return reduce(lambda a, b: a ^ b, nums)

if __name__ == "__main__":
    solution = Solution()
    print solution.singleNumber([1, 2, 3, 2, 1])
