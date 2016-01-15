/* Given a sorted array, remove the duplicates in place such that 
 * each element appear only once and return the new length.
 * Do not allocate extra space for another array, you must do this 
 * in place with constant memory.
 * For example, given input array nums = [1,1,2],
 * Your function should return length = 2, with the first two 
 * elements of nums being 1 and 2 respectively. 
 * It doesn't matter what you leave beyond the new length.
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    for (var current = 0, i = 0; i < nums.length; ++i) {
        if (current == 0 || nums[i] > nums[current - 1]) {
            nums[current++] = nums[i]
        }
    }
    return current
};
