/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    nums.sort(function(a, b) { return b - a; });
    var large = nums.slice(), mid = Math.floor(nums.length / 2);
    var small = large.splice(mid, nums.length - mid);
    for (var i = 0, j = 0, k = 0; i < nums.length; i++)
        nums[i] = i % 2 === 0 ? small[j++] : large[k++];
};
