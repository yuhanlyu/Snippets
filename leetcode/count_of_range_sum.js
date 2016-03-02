/* Given an integer array nums, return the number of range sums that lie in 
 * [lower, upper] inclusive.
 * Range sum S(i, j) is defined as the sum of the elements in nums between 
 * indices i and j (i ≤ j), inclusive.
 * Time Complexity: O(n lg n)
 * Space Complexity: O(n)
 */


/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countRangeSum = function(nums, lower, upper) {
    function sort(left, right) {
        if (right - left <= 1) 
            return 0;
        var mid = left + Math.floor((right - left) / 2);
        var result = sort(left, mid) + sort(mid, right);
        var j = mid, k = mid, t = mid;
        var temp = new Array(right - left);
        for (var i = left, r = 0; i < mid; ) {
            while (k < right && prefix[k] - prefix[i] < lower) 
                k++;
            while (j < right && prefix[j] - prefix[i] <= upper) 
                j++;
            while (t < right && prefix[t] < prefix[i]) 
                temp[r++] = prefix[t++];
            temp[r++] = prefix[i++];
            result += j - k;
        }
        for (i = 0; i < t - left; ++i)
            prefix[left + i] = temp[i];
        return result;
    }
    prefix = [0];
    for (var num of nums)
        prefix.push(prefix[prefix.length - 1] + num);
    return sort(0, prefix.length);
};
