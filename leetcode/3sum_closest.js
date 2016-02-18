/* Given an array S of n integers, find three integers in S such that the sum 
 * is closest to a given number, target. Return the sum of the three integers. 
 * You may assume that each input would have exactly one solution.
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort(function(a, b) {return a - b});
    var result = nums[0] + nums[1] + nums[2];
    for (var i = 0; i < nums.length - 2; ++i) {
        for (var left = i + 1, right = nums.length - 1; left < right; ) {
            sum = nums[i] + nums[left] + nums[right];
            if (Math.abs(sum - target) < Math.abs(result - target))
                result = sum;
            if (sum <= target)
                left += 1;
            else
                right -= 1;
        }
    }
    return result;
};
