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
        var mid = left + Math.floor((right - left) / 2)
        if (nums[mid] === target)
            return true
        if (nums[left] === nums[mid] && nums[mid] === nums[right]) {
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
