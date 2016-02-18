class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        right, cur = [-2 ** 31] * (len(nums) + 1), 0
        for i in xrange(len(nums) - 1, -1, -1):
            cur += nums[i]
            right[i] = max(right[i + 1], cur)
            if cur < 0:
                cur = 0
        result, cur = -2 ** 31, 0
        for i, x in enumerate(nums):
            cur += x
            result = max(result, cur + right[i + 1])
            if cur < 0:
                cur = 0
        return result
