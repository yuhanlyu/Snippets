/* Given an array of n positive integers and a positive integer s, find the 
 * minimal length of a subarray of which the sum >= s. If there isn't one, 
 * return 0 instead.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(s, nums) {
    var result = null, begin = 0, sum = 0;
    for (var i = 0; i < nums.length; ++i) {
        for (sum += nums[i]; sum >= s; sum -= nums[begin++]) {
            if (!result || i - begin + 1 < result)
                result = i - begin + 1;
        }
    }
    return result ? result : 0;
};
