/* Given an unsorted array of integers, find the length of the longest 
 * consecutive elements sequence.
 * Time Complexity: O(n) in average
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    var b = new Map(), result = 0;
    for (var num of nums) {
        if (!b.has(num)) {
            var left = b.has(num - 1) ? b.get(num - 1) : num;
            var right = b.has(num + 1) ? b.get(num + 1) : num;
            result = Math.max(result, right - left + 1);
            b.set(num, num);
            b.set(left, right);
            b.set(right, left);
        }
    }
    return result;
};
