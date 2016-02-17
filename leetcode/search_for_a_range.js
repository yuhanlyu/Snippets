/* Given a sorted array of integers, find the starting and ending position of a 
 * given target value.
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * If the target is not found in the array, return [-1, -1].
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    function bsearch(nums, target) {
        for (var left = 0, right = nums.length - 1; left <= right; ) {
            mid = left + Math.floor((right - left) / 2)
            if (nums[mid] < target)
                left = mid + 1
            else
                right = mid - 1
        }
        return left
    }
    lower = bsearch(nums, target)
    if (lower == nums.length || nums[lower] != target)
        return [-1, -1]
    return [lower, bsearch(nums, target + 1) - 1]
};
