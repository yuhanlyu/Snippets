class Solution:
    # @param nums: a list of integer
    # @return: return nothing (void), do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):
        pivot = len(nums) - 1
        while pivot > 0 and nums[pivot - 1] >= nums[pivot]:
            pivot = pivot - 1
        if pivot == 0:
            nums.reverse()
        else:
            num, index = nums[pivot - 1], len(nums) - 1
            while nums[index] <= num:
                index = index - 1
            nums[index], nums[pivot - 1] = nums[pivot - 1], nums[index]
            for i in xrange((len(nums) - pivot) / 2):
                nums[pivot + i], nums[~i] = nums[~i], nums[pivot + i]
