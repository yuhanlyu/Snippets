/* Given an array and a value, remove all instances of that value in place 
 * and return the new length.
 * The order of elements can be changed. 
 * It doesn't matter what you leave beyond the new length.
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    for (var current = 0, i = 0; i < nums.length; ++i) {
        if (nums[i] != val) {
            nums[current++] = nums[i]
        }
    }
    return current
};
