/* Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 
 * as one sorted array.
 * Time Complexity: O(m + n)
 * Space Complexity: O(1)
 */
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    for (--m, --n; m >= 0 && n >= 0;) {
        if (nums1[m] >= nums2[n]) {
            nums1[m + n + 1] = nums1[m]
            --m
        } else {
            nums1[m + n + 1] = nums2[n]
            --n
        }
    }
    for (; n >= 0; --n)
        nums1[n] = nums2[n]
};
