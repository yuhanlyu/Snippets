# Given an array of integers, find out whether there are two distinct indices 
# i and j in the array such that the difference between nums[i] and nums[j] is 
# at most t and the difference between i and j is at most k.
# Time Complexity: O(n) in average
# Space Complexity: O(n)

import collections

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        indices = collections.OrderedDict()
        for index, num, key in ((i, n, n/(t+1)) for (i, n) in enumerate(nums)):
            for neighbor in (key - 1, key, key + 1):
                if neighbor in indices and abs(indices[neighbor] - num) <= t:
                    return True
            indices[key] = num
            if len(indices) == k + 1: indices.popitem(False)
        return False

if __name__ == "__main__":
    solution = Solution()
    print solution.containsNearbyAlmostDuplicate([2, 1], 1, 1)
