/* Given an array of non-negative integers, you are initially positioned at the 
 * first index of the array.
 * Each element in the array represents your maximum jump length at that 
 * position.
 * Determine if you are able to reach the last index.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    for (var i = 0, m = 0; i < nums.length && i <= m; ++i)
        m = Math.max(m, i + nums[i]);
    return i == nums.length;
};
