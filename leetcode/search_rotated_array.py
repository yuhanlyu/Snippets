# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its 
# index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target: return mid
            if (nums[mid] <= nums[right] and nums[mid] < target <= nums[right])\
            or (nums[mid] > nums[right] and 
            not nums[left] <= target < nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    print solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print solution.search([4, 5, 6, 7, 0, 1, 2], 4)
    print solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    print solution.search([4, 5, 6, 7, 0, 1, 2], 6)
