# Given an array with n objects colored red, white or blue, sort them so 
# that objects of the same color are adjacent, with the colors in the order 
# red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color 
# red, white, and blue respectively.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1 
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


if __name__ == "__main__":
    solution = Solution()
    list = [0, 1, 2, 0, 2, 1, 1, 0]
    solution.sortColors(list)
    print list
