/* Given a sorted positive integer array nums and an integer n, add/patch 
 * elements to the array such that any number in range [1, n] inclusive can be 
 * formed by the sum of some elements in the array. Return the minimum number 
 * of patches required.
 * Time Complexity: O(nums.length + lg n):
 * Space Complexity: O(1)
 */


/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
 */
var minPatches = function(nums, n) {
    for (var miss = 1, result = 0, i = 0; miss <= n; ) {
        if (i < nums.length && nums[i] <= miss)
            miss += nums[i++];
        else {
            miss *= 2;
            ++result;
        }
    }
    return result;
};
