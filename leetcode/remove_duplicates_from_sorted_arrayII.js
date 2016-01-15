/* Follow up for "Remove Duplicates":
 * What if duplicates are allowed at most twice?
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    for (var current = 0, i = 0; i < nums.length; ++i) {
        if (current < 2 || nums[i] > nums[current - 2]) {
            nums[current++] = num
        }
    }    
    return current
};
