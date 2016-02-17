/* Given an array where elements are sorted in ascending order, 
 * convert it to a height balanced BST.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    function helper(nums, begin, end) {
        if (begin === end)
            return null
        var mid = begin + Math.floor((end - begin) / 2)
        var root = new TreeNode(nums[mid])
        root.left = helper(nums, begin, mid)
        root.right = helper(nums, mid + 1, end)
        return root
    }
    return helper(nums, 0, nums.length)
};
