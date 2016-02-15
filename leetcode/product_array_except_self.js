/* Given an array of n integers where n > 1, nums, return an array output such 
 * that output[i] is equal to the product of all the elements of nums except 
 * nums[i]. Solve it without division and in O(n).
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    result = new Array(nums.length)
    result[0] = 1
    for (var index = 1; index < nums.length; ++index)
        result[index] = nums[index - 1] * result[index - 1]
    for (var product = 1, index = nums.length - 1; index >= 0; --index) {
        result[index] *= product
        product *= nums[index]
    }
    return result
};
