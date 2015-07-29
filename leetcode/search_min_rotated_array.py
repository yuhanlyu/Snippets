# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            print nums[left], nums[right]
            if nums[left] <= nums[right]: return nums[left]
            mid = left + (right - left) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid

if __name__ == "__main__":
    solution = Solution()
    print solution.findMin([3, 1, 2])
    #print solution.findMin([4, 5, 6, 7, 0, 1, 2])
