class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        result = cur_min = cur_max = nums[0]
        for i in xrange(1, len(nums)):
            (cur_min, _, cur_max) = sorted([nums[i],
                                    nums[i] * cur_min, nums[i] * cur_max])
            result = max(result, cur_max)
        return result
