/* Given an array of integers, find two numbers such that they add up to a 
 * specific target number.
 * Time Complexity: O(n) in average
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (var elements = {}, i = 0; i < nums.length; ++i)
        elements[nums[i]] = i
    for (i = 0; i < nums.length; ++i)
        if (target - nums[i] in elements && i !== elements[target - nums[i]])
            return [i, elements[target - nums[i]]]
};
