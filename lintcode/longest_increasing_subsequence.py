import bisect
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        ends = [float('inf')] * (len(nums) + 1)
        for num in nums:
            ends[bisect.bisect_right(ends, num)] = num
        return min(len(nums), ends.index(float('inf')) - 1)
