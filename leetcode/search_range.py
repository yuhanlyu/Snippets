# Given a sorted array of integers, find the starting and ending position of a 
# given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        def bsearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        lower = bsearch(nums, target)
        if lower == len(nums) or nums[lower] != target: return [-1, -1]
        return [lower, bsearch(nums, target + 1) - 1]

if __name__ == "__main__":
    solution = Solution()
    print solution.searchRange([5, 7, 7, 8, 8, 10], 8)
