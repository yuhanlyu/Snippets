# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# The array may contain duplicates.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]: return nums[left]
            mid = left + (right - left) / 2
            if nums[mid] > max(nums[left], nums[right]):
                left = mid + 1
            elif nums[mid] != nums[left]:
                right = mid 
            else:
                left += 1
        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    print solution.findMin([4, 5, 6, 7, 0, 1, 2])
