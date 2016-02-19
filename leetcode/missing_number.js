/* Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
 * find the one that is missing from the array.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    for (var xor = 0, i = 0; i < nums.length; ++i)
        xor ^= i ^ nums[i];
    return xor ^ nums.length;
};
