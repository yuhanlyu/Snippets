# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target: return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif (nums[left] <= target < nums[mid]) or (nums[left] > nums[mid] 
                  and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print solution.search([4, 5, 6, 7, 0, 1, 2], 4)
    print solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    print solution.search([4, 5, 6, 7, 0, 1, 2], 6)
