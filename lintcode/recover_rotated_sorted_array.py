class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        point = -1
        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                point = i
                break
        reverse(nums, 0, point)
        reverse(nums, point + 1, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)
