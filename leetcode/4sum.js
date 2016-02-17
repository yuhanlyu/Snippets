/* Given an array S of n integers, are there elements a, b, c, and d in S 
 * such that a + b + c + d = target? Find all unique quadruplets in the array 
 * which gives the sum of target.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    unique = {}
    nums.sort(function(a,b){return a - b})
    for (var i = 0; i < nums.length - 3; ++i) {
        for (var j = i + 1; j < nums.length - 2; ++j) {
            var k = nums[i] + nums[j]
            for (var left = j + 1, right = nums.length - 1; left < right; ) {
                s = k + nums[left] + nums[right]
                if (s == target) {
                    unique[[nums[i], nums[j], nums[left], nums[right]]] = true
                    ++left
                    --right
                } else if (s < target)
                    ++left
                else
                    --right
            }
        }
    }
    result = []
    for (var key in unique) {
        var array = key.split(",")
        for (var i = 0; i < 4; ++i)
            array[i] = parseInt(array[i])
        result.push(array)
    }
    return result
};
