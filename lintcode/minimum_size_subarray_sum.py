class Solution:
    # @param nums: a list of integers
    # @param s: an integer
    # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        result, begin, sum = None, 0, 0
        for i, num in enumerate(nums):
            sum += num
            while sum >= s:
                if not result or i - begin + 1 < result: result = i - begin + 1
                sum -= nums[begin]
                begin += 1
        return result if result else -1
