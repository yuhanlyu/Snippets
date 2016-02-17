/* Find the contiguous subarray within an array (containing at least one number)
 * which has the largest sum.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var result = nums[0], cur = 0           
    for (var x of nums) {
        cur += x
        result = Math.max(result, cur)
        if (cur < 0)
            cur = 0
    }
    return result
};
