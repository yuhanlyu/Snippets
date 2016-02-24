class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if len(d) >= k:
                d = dict([(a, c - 1) for (a, c) in d.iteritems() if c > 1])
        return [num for num in d if nums.count(num) > len(nums) / k][0]
