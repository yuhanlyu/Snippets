class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        K = {}
        for num in nums:
            K[num] = K.get(num, 0) + 1
            if len(K) >= 3:
                K = dict([(a, c - 1) for (a, c) in K.iteritems() if c > 1])
        return [num for num in K if nums.count(num) > len(nums) / 3][0]
