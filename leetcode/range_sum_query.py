# Given an integer array nums, find the sum of the elements between indices i 
# and j (i <= j), inclusive.
# Time Complexity: O(1) per query
# Space Complexity: O(n)

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.prefix = [0]
        for i in xrange(len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix[j + 1] - self.prefix[i]
