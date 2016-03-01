/* Given an integer array nums, find the sum of the elements between indices i 
 * and j (i <= j), inclusive.
 * The update(i, val) function modifies nums by updating the element at index i 
 * to val.
 * Time Complexity: O(lg n)
 * Space Complexity: O(n)
 */

/**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.nums = new Array(nums.length);
    this.tree = new Array(nums.length);
    this.nums.fill(0);
    this.tree.fill(0);
    for (var i = 0; i < nums.length; ++i)
        this.update(i, nums[i]);
};

/**
 * @param {number} i
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function(i, val) {
    var d = val - this.nums[i];
    this.nums[i] = val;
    for (; i < this.nums.length; i |= i + 1)
        this.tree[i] += d;
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.sum(j) - this.sum(i - 1);
};

NumArray.prototype.sum = function(i) {
    for (var ans = 0; i >= 0; i = (i & (i + 1)) - 1)
        ans += this.tree[i];
    return ans;
};



/**
 * Your NumArray object will be instantiated and called as such:
 * var numArray = new NumArray(nums);
 * numArray.sumRange(0, 1);
 * numArray.update(1, 10);
 * numArray.sumRange(0, 2);
 */
