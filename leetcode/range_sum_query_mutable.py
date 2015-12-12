# Given an integer array nums, find the sum of the elements between indices i 
# and j (i <= j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i 
# to val.
# Time Complexity: O(lg n)
# Space Complexity: O(n)

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums, self.tree = [0] * len(nums), [0] * len(nums)
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        d = val - self.nums[i]
        self.nums[i] = val
        while i < len(self.nums):
            self.tree[i] += d
            i |= i + 1

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)

    def sum(self, i):
        ans = 0
        while i >= 0:
            ans += self.tree[i]
            i = (i & (i + 1)) - 1
        return ans

# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 2, 3])
print numArray.sumRange(0, 1)
numArray.update(1, 10)
print numArray.sumRange(1, 2)
