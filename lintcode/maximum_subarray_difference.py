class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        right_min, cur_min = [2 ** 31] * (len(nums) + 1), 0
        right_max, cur_max = [-2 ** 31] * (len(nums) + 1), 0
        for i in xrange(len(nums) - 1, -1, -1):
            cur_min, cur_max = nums[i] + cur_min, nums[i] + cur_max
            right_min[i] = min(right_min[i + 1], cur_min)
            right_max[i] = max(right_max[i + 1], cur_max)
            if cur_min > 0:
                cur_min = 0
            if cur_max < 0:
                cur_max = 0
        result, cur_min, cur_max = -2 ** 31, 0, 0
        for i in xrange(len(nums) - 1):
            cur_min, cur_max = nums[i] + cur_min, nums[i] + cur_max
            diff1 = abs(cur_max - right_min[i + 1])
            diff2 = abs(cur_min - right_max[i + 1])
            result = max(result, diff1, diff2)
            if cur_max < 0:
                cur_max = 0
            if cur_min > 0:
                cur_min = 0
        return result
