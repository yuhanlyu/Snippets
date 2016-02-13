/* Invert a binary tree.
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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root) {
        var temp = invertTree(root.right)
        root.right = invertTree(root.left)
        root.left = temp
    }
    return root
};
