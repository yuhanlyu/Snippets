class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        count = 0
        for x in nums:
            if count == 0:
                candidate, count = x, 1
            else:
                count += (1 if x == candidate else -1)
        return candidate
