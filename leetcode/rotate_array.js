/* Rotate an array of n elements to the right by k steps.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    function reverse(nums, begin, end) {
        for (; begin < end; ++begin, --end) {
            var temp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = temp
        }
    }    
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
};
