/* Given an array of integers, every element appears twice except for one. 
 * Find that single one.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    return nums ? nums.reduce(function(a, b){ return a ^ b}) : 0
};
