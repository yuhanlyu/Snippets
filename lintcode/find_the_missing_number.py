class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        xor = 0
        for (i, num) in enumerate(nums):
            xor ^= i
            xor ^= num
        return xor ^ len(nums)
