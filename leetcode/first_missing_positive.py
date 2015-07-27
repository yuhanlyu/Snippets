# Given an unsorted integer array, find the first missing positive integer.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in xrange(len(nums)):
            num = nums[i]
            while num <= len(nums) and num > 0 and nums[num - 1] != num:
                nums[num-1], nums[i], num = nums[i], nums[num-1], nums[num-1]
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == "__main__":
    solution = Solution()
    print solution.firstMissingPositive([1,2,0])
    print solution.firstMissingPositive([3,4,-1,1])
