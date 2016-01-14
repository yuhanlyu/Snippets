class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 1:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
