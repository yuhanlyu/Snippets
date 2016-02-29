/*You are given an integer array nums and you have to return a new counts array.
 * The counts array has the property where counts[i] is the number of smaller 
 * elements to the right of nums[i].
 * Time Complexity: O(n lg n)
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countSmaller = function(nums) {
    function sort(nums) {
        var mid = Math.floor(nums.length / 2);
        if (mid > 0) {
            var left = sort(nums.slice(0, mid)), right = sort(nums.slice(mid));
            for (var i = nums.length - 1; i >= 0; --i) {
                if (right.length === 0 
                || (left.length > 0 && left[left.length - 1][1] > right[right.length - 1][1])) {
                    result[left[left.length - 1][0]] += right.length;
                    nums[i] = left.pop();
                } else
                    nums[i] = right.pop();
            }
        }
        return nums;
    }
    var result = new Array(nums.length);
    result.fill(0);
    var temp = new Array(nums.length);
    for (var i = 0; i < nums.length; ++i)
        temp[i] = [i, nums[i]];
    sort(temp);
    return result;
};
