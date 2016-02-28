/* Given a binary tree, find the lowest common ancestor (LCA) of two given 
 * nodes in the tree.
 * Time Complexity: O(n)
 * Space Complexity: O(h), h is the height of tree
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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    if ([null, p, q].indexOf(root) >= 0)
        return root;
    var left = lowestCommonAncestor(root.left, p, q);
    var right = lowestCommonAncestor(root.right, p, q);
    if (left && right)
        return root;
    return left ? left : right;
};
