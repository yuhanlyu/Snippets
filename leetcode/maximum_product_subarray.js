/* Find the contiguous subarray within an array (containing at least one number)
 * which has the largest product.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    var cur_min = nums[0], cur_max = nums[0];
    for (var result = nums[0], i = 1; i < nums.length; ++i) {
        var temp = cur_min;
        cur_min = Math.min(nums[i], nums[i] * cur_min, nums[i] * cur_max);
        cur_max = Math.max(nums[i], nums[i] * temp, nums[i] * cur_max);
        result = Math.max(result, cur_max);
    }
    return result;
};
