class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        map, cur = {0:-1}, 0
        for i, x in enumerate(nums):
            cur += x
            if cur in map:
                return [map[cur] + 1, i]
            map[cur] = i
