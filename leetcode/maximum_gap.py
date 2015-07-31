# Given an unsorted array, find the maximum difference between the successive 
# elements in its sorted form.
# Try to solve it in linear time/space.
# Return 0 if the array contains less than 2 elements.
# You may assume all elements in the array are non-negative integers and fit 
# in the 32-bit signed integer range.
# Time Complexity: O(n)
# Space Complexity: O(n)

from math import floor

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if not nums or len(nums) == 1: return 0
        lb, width = min(nums), (max(nums) - min(nums)) / (len(nums) - 1.0)
        bucket = [[None, None] for _ in xrange(len(nums))]
        for num in nums:
            tuple = bucket[int(floor((num - lb) / width))]
            tuple[0] = num if not tuple[0] else min(num, tuple[0])
            tuple[1] = num if not tuple[1] else max(num, tuple[1])
        bucket[:] = [tuple for tuple in bucket if tuple[0]]
        return max(bucket[i][0]-bucket[i-1][1] for i in xrange(1, len(bucket)))

if __name__ == "__main__":
    solution = Solution()
    print solution.maximumGap([1, 3, 5, 8, 9])
