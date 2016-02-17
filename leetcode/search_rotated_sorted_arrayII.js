/* Follow up for "Search in Rotated Sorted Array":
 * What if duplicates are allowed?
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    for (var left = 0, right = nums.length - 1; left <= right;) {
        mid = left + Math.floor((right - left) / 2)
        if (nums[mid] == target)
            return true
        if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
            ++left
            --right
        } else if ((nums[left] <= target && target < nums[mid])
        || (nums[left] > nums[mid] 
        && !(nums[mid] < target && target <= nums[right])))
            right = mid - 1
        else
            left = mid + 1
    }   
    return false
};

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
