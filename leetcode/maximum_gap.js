/* Given an unsorted array, find the maximum difference between the successive 
 * elements in its sorted form.
 * Try to solve it in linear time/space.
 * Return 0 if the array contains less than 2 elements.
 * You may assume all elements in the array are non-negative integers and fit 
 * in the 32-bit signed integer range.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumGap = function(nums) {
    if (nums.length <= 1)
        return 0;
    var lb = Math.min.apply(Math, nums);
    var width = (Math.max.apply(Math, nums) - lb) / (nums.length - 1);
    if (width === 0)
        return 0;
    for (var bucket = [], i = 0; i < nums.length; ++i)
        bucket.push([null, null]);
    for (var num of nums) {
        var tuple = bucket[Math.floor((num - lb) / width)];
        tuple[0] = tuple[0] === null ? num : Math.min(num, tuple[0]);
        tuple[1] = tuple[1] === null ? num : Math.max(num, tuple[1]);
    }
    var result = [];
    for (tuple of bucket)
        if (tuple[0] !== null)
            result.push(tuple);
    var max = 0;
    for (i = 1; i < result.length; ++i)
        if (result[i][0] - result[i - 1][1] > max)
            max = result[i][0] - result[i - 1][1];
    return max;
};
