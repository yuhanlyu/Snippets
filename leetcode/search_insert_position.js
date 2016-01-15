/* Given a sorted array and a target value, return the index if the target is 
 * found. If not, return the index where it would be if it were inserted in 
 * order.
 * You may assume no duplicates in the array.
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    for (var left = 0, right = nums.length - 1; left <= right; ) {
        var mid = left + Math.floor((right - left) / 2)
        if (nums[mid] < target)
            left = mid + 1
        else
            right = mid - 1
    }
    return left
};
