/* There are two sorted arrays nums1 and nums2 of size m and n respectively. 
 * Find the median of the two sorted arrays. The overall run time complexity 
 * should be O(log (m+n)).
 * Time Complexity: O(lg (m + n))
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    function findk(nums1, nums2, K) {
        if (nums2.length === 0) return nums1[K - 1];
        for (var left = 0, right = nums1.length - 1; left <= right; ) {
            var mid1 = left + Math.floor((right - left) / 2);
            var mid2 = K - mid1 - 1;
            if (mid2 === nums2.length && nums1[mid1] >= nums2[nums2.length - 1])
                return nums1[mid1];
            if (mid2 === 0 && nums1[mid1] <= nums2[0])
                return nums1[mid1];
            if (mid2 >= nums2.length)
                left = mid1 + 1;
            else if (mid2 <= 0)
                right = mid1 - 1;
            else if (nums2[mid2 - 1] > nums1[mid1])
                left = mid1 + 1;
            else if (nums2[mid2] < nums1[mid1])
                right = mid1 - 1;
            else if (nums2[mid2 - 1] <= nums1[mid1] && nums1[mid1] <= nums2[mid2])
                return nums1[mid1];
            else
                return null;
        }
    }
    var N1 = nums1.length, N2 = nums2.length;
    var K = Math.floor((N1 + N2) / 2) + (N1 + N2) % 2;
    var num1 = findk(nums1, nums2, K);
    if (!num1)
        num1 = findk(nums2, nums1, K);
    if ((N1 + N2) % 2 === 1)
        return num1;
    var num2 = findk(nums1, nums2, K + 1);
    if (!num2)
        num2 = findk(nums2, nums1, K + 1);
    return (num1 + num2) / 2;
};
