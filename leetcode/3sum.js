/* Given an array S of n integers, are there elements a, b, c in S such that 
 * a + b + c = 0? 
 * Find all unique triplets in the array which gives the sum of zero.
 * Time Complexity: O(n^2)
 * Space Complexity: O(output) assuming sorting in place
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    result = []
    nums.sort(function(a,b){return a - b})
    for (var i = 0; i < nums.length - 2; ++i) {
        if (i === 0 || nums[i] !== nums[i - 1]) {
            for (var left = i + 1, right = nums.length - 1; left < right; ) {
                if (nums[i] + nums[left] + nums[right] === 0) {
                    result.push([nums[i], nums[left], nums[right]])
                    var t = nums[left]
                    while (left < right && nums[left] === t)
                        ++left
                    t = nums[right]
                    while (left < right && nums[right] === t)
                        --right
                } else if (nums[i] + nums[left] + nums[right] < 0)
                    ++left
                else
                    --right
            }
        }
    }
    return result
};
