/* Given an array with n objects colored red, white or blue, sort them so 
 * that objects of the same color are adjacent, with the colors in the order 
 * red, white and blue.
 * Here, we will use the integers 0, 1, and 2 to represent the color 
 * red, white, and blue respectively.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for (var left = 0, mid = 0, right = nums.length - 1; mid <= right; ) {
        if (nums[mid] === 0) {
            var tmp = nums[mid];
            nums[mid] = nums[left];
            nums[left] = tmp;
            ++mid;
            ++left;
        } else if (nums[mid] === 1)
            ++mid;
        else {
            tmp = nums[mid];
            nums[mid] = nums[right];
            nums[right] = tmp;
            --right;
        }
    }
};
