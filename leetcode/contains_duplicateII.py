# Given an array of integers and an integer k, find out whether 
# there are two distinct indices i and j in the array such that 
# nums[i] = nums[j] and the difference between i and j is at most k.
# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, x in enumerate(nums):
            if x in window:
                return True;
            window.add(x)
            if i >= k:
                window.remove(nums[i - k])
        return False

if __name__ == "__main__":
    solution = Solution()
    print solution.containsNearbyDuplicate([1, 0, 1], 2)
