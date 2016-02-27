/* Given a binary tree, find the maximum path sum.  
 * The path may start and end at any node in the tree.
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
 * @return {number}
 */
var maxPathSum = function(root) {
    function helper(root) {
        if (!root)
            return [null, 0];
        var left = helper(root.left);
        var right = helper(root.right);
        var first = left[0];
        if (!first || (right[0] && right[0] > first))
            first = right[0];
        if (!first || (left[1] + right[1] + root.val > first))
            first = left[1] + right[1] + root.val;
        return [first, Math.max(0, root.val + Math.max(left[1], right[1]))];
    }
    return helper(root)[0];
};
