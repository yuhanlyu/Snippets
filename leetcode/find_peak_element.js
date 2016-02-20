/* A peak element is an element that is greater than its neighbors.
 * Given an input array where num[i] != num[i+1], find a peak element and 
 * return its index.
 * The array may contain multiple peaks, in that case return the index to any 
 * one of the peaks is fine.
 * You may imagine that num[-1] = num[n] = -infty
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    for (var left = 0, right = nums.length - 1; left < right; ) {
        var mid = left + Math.floor((right - left) / 2);
        if (nums[mid] > nums[mid + 1])
            right = mid;
        else
            left = mid + 1;
    }
    return left;
};
