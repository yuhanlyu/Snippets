/* Given an integer array nums, find the sum of the elements between indices i 
 * and j (i <= j), inclusive.
 * Time Complexity: O(1) per query
 * Space Complexity: O(n)
 */

/**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.prefix = [0];
    for (var num of nums)
        this.prefix.push(this.prefix[this.prefix.length - 1] + num);
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.prefix[j + 1] - this.prefix[i];
};


/**
 * Your NumArray object will be instantiated and called as such:
 * var numArray = new NumArray(nums);
 * numArray.sumRange(0, 1);
 * numArray.sumRange(0, 2);
 */
