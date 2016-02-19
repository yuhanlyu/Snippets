/* Given an array of non-negative integers, you are initially positioned at the 
 * first index of the array.
 * Each element in the array represents your maximum jump length at that 
 * position.
 * Your goal is to reach the last index in the minimum number of jumps.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    for (var m = 0, next = 0, jump = 0, i = 0; i < nums.length - 1; ++i) {
        next = Math.max(next, i + nums[i]);
        if (i === m) {
            ++jump;
            m = next;
        }
    }
    return jump;
};
