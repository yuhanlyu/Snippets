class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        nums.sort()
        result = [list(nums)]
        while True:
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i < 0: break
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = nums[-1:i:-1]
            result.append(list(nums))
        return result
