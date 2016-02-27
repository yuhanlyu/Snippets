/* Given a set of distinct integers, nums, return all possible subsets.
 * Time Complexity: O(n2^n)
 * Space Complexity: O(n2^n)
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    nums.sort(function (a, b) { return a - b; });
    for (var result = [], x = 0; x < (1 << nums.length); ++x) {
        for (var temp = [], i = 0; i < nums.length; ++i)
            if ((x >> i) & 1 == 1)
                temp.push(nums[i]);
        result.push(temp);
    }
    return result;
};
