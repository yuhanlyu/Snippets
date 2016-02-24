/* Implement next permutation, which rearranges numbers into the 
 * lexicographically next greater permutation of numbers.
 * If such arrangement is not possible, it must rearrange it as the lowest 
 * possible order (ie, sorted in ascending order).
 * The replacement must be in-place, do not allocate extra memory.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    var pivot = nums.length - 1;
    while (pivot > 0 && nums[pivot - 1] >= nums[pivot])
        --pivot;
    if (pivot === 0)
        nums.reverse();
    else {
        var num = nums[pivot - 1];
        for (var index = nums.length - 1; nums[index] <= num; --index)
            ;
        nums[pivot - 1] = nums[index];
        nums[index] = num;
        for (var i = 0; i < Math.floor((nums.length - pivot) / 2); ++i) {
            var tmp = nums[nums.length - i - 1];
            nums[nums.length - i - 1] = nums[pivot + i];
            nums[pivot + i] = tmp;
        }
    }
};
