/* Find the kth largest element in an unsorted array. 
 * Note that it is the kth largest element in the sorted order, not the kth 
 * distinct element.
 * Time Complexity: O(n) in average
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    function search(nums, k, left, right) {
        var pivot = nums[right];
        for (var begin = left, end = right; true; ) {
            while (nums[left] < pivot && left < right)
                ++left;
            while (nums[right] >= pivot && left < right)
                --right;
            if (left >= right)
                break;
            var tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
        }
        tmp = nums[left];
        nums[left] = nums[end];
        nums[end] = tmp;
        if (k === (left - begin) + 1)
            return nums[left];
        if (k < (left - begin) + 1)
            return search(nums, k, begin, left - 1);
        return search(nums, k - (left - begin + 1), left + 1, end);
    }
    return search(nums, nums.length - k + 1, 0, nums.length - 1);
};
