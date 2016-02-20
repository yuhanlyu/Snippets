/* Given an unsorted array of integers, find the length of longest increasing 
 * subsequence.
 * Time Complexity: O(n lg n)
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    var ends = new Array(nums.length + 1);
    ends.fill(Infinity);
    for (var num of nums) {
        for (var left = 0, right = nums.length - 1; left <= right;) {
            var mid = left + Math.floor((right - left) / 2);
            if (ends[mid] < num)
                left = mid + 1;
            else
                right = mid - 1;
        }
        ends[left] = num
    }
    return Math.min(nums.length, ends.indexOf(Infinity));
};
