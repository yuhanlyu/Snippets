/* Given an unsorted integer array, find the first missing positive integer.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    for (var i = 0; i < nums.length; ++i) {
        var num = nums[i] - 1; 
        while (0 <= num && num < nums.length && nums[num] != num + 1) {
            var temp1 = nums[i], temp2 = nums[num];
            nums[num] = temp1;
            nums[i] = temp2;
            num = temp2 - 1;
        }
    }
    for (i = 0; i < nums.length; ++i) {
        if (nums[i] != i + 1)
            return i + 1;
    }
    return nums.length + 1;
};
