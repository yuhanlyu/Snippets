# Given an array of integers, every element appears three times except for one. # Find that single one.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one, two = 0, 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one

if __name__ == "__main__":
    solution = Solution()
    print solution.singleNumber([1, 2, 3, 2, 2, 1, 1])
