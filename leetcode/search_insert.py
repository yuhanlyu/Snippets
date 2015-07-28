# Given a sorted array and a target value, return the index if the target is 
# found. If not, return the index where it would be if it were inserted in 
# order.
# You may assume no duplicates in the array.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    solution = Solution()
    print solution.searchInsert([1,3,5,6], 5)
    print solution.searchInsert([1,3,5,6], 2)
    print solution.searchInsert([1,3,5,6], 7)
    print solution.searchInsert([1,3,5,6], 0)
