class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        prefix, cur, min_value, result = [None] * len(nums), 0, 2 ** 32, [0, 0]
        for i, num in enumerate(nums):
            cur += num
            prefix[i] = (cur, i)
        prefix.sort()
        for i in xrange(len(nums) - 1):
            if abs(prefix[i + 1][0] - prefix[i][0]) < min_value:
                min_value = abs(prefix[i + 1][0] - prefix[i][0])
                result[0] = min(prefix[i][1], prefix[i + 1][1]) + 1
                result[1] = max(prefix[i][1], prefix[i + 1][1])
        return result
