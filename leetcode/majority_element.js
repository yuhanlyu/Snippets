/* Given an array of size n, find the majority element. 
 * The majority element is the element that appears more than n/2 times.
 * You may assume that the array is non-empty and 
 * the majority element always exist in the array.
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    for (var count = 0, i = 0; i < nums.length; ++i) {
        if (count)
            count += (nums[i] == candidate ? 1 : -1)
        else {
            candidate = nums[i]
            count = 1
        }
    }
    return candidate
};
