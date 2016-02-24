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
        if (!(num in b)) {
            var left = num - 1 in b ? b[num - 1] : num;
            var right = num + 1 in b ? b[num + 1] : num;
            result = Math.max(result, right - left + 1);
            b[num] = num;
            b[left] = right;
            b[right] = left;
        }
    }
    return result;
};
