/* Given a binary tree, determine if it is height-balanced.
 * For this problem, a height-balanced binary tree is defined as a binary tree 
 * in which the depth of the two subtrees of every node never differ by more 
 * than 1.
 * Time Complexity: O(n)
 * Space Complexity: O(h), h is the height of the tree
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    function helper(root) {
        if (!root)
            return 0;
        var left_height = helper(root.left);
        if (left_height < 0)
            return -2;
        var right_height = helper(root.right);
        if (Math.abs(left_height - right_height) > 1) 
            return -2;
        return 1 + Math.max(left_height, right_height);
    }
    return helper(root) >= 0;
};
