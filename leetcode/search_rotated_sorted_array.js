/* Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * You are given a target value to search. If found in the array return its 
 * index, otherwise return -1.
 * You may assume no duplicate exists in the array.
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    for (var left = 0, right = nums.length - 1; left <= right; ) {
        mid = left + Math.floor((right - left) / 2)
        if (nums[mid] == target)
            return mid
        if ((nums[mid] <= nums[right] && nums[mid] < target 
                                                  && target <= nums[right]) 
         || (nums[mid] > nums[right] && !(nums[left] <= target 
                                                     && target < nums[mid])))
           left = mid + 1 
        else
            right = mid - 1
    }   
    return -1
};
