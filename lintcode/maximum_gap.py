from math import floor

class Solution:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        if not nums or len(nums) == 1: return 0
        lb, width = min(nums), (max(nums) - min(nums)) / (len(nums) - 1.0)
        if width == 0: return 0
        bucket = [[None, None] for _ in xrange(len(nums))]
        for num in nums:
            tuple = bucket[int(floor((num - lb) / width))]
            tuple[0] = num if not tuple[0] else min(num, tuple[0])
            tuple[1] = num if not tuple[1] else max(num, tuple[1])
        bucket[:] = [tuple for tuple in bucket if tuple[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in xrange(1, len(bucket)))
