/* Given two arrays of length m and n with digits 0-9 representing two numbers.
 * Create the maximum number of length k <= m + n from digits of the two. The 
 * relative order of the digits from the same array must be preserved. Return 
 * an array of the k digits. You should try to optimize your time and space 
 * complexity.
 * Time Complexity: O(n^3)
 * Space Complexity: O(n)
 */


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[]}
 */
var maxNumber = function(nums1, nums2, k) {
    function pick(a, k) {
        var result = new Array(k);
        for (var i = 0, j = 0; i < a.length; ++i) {
            while (a.length - i + j > k && j > 0 && result[j - 1] < a[i]) 
                --j;
            if (j < k) 
                result[j++] = a[i];
        }
        return result;
    }
    function greater(a, i, b, j) {
        while (i < a.length && j < b.length && a[i] == b[j]) {
            i++;
            j++;
        }
        return j == b.length || (i < a.length && a[i] > b[j]);
    }
    function merge(a, b) {
        for (var result = [], i = 0, j = 0; result.length < k;)
            result.push(greater(a, i, b, j) ? a[i++] : b[j++]);
        return result;
    }
    var result;
    for (var i = Math.max(k - nums2.length, 0); i < Math.min(k, nums1.length) + 1; ++i) {
        var temp = merge(pick(nums1, i), pick(nums2, k - i));
        if (!result || greater(temp, 0, result, 0))
            result = temp;
    }
    return result;
};
