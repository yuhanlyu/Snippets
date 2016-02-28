/* Given preorder and inorder traversal of a tree, construct the binary tree.
 * Time Complexity: O(n)
 * Space Complexity: O(n), O(h) is achievable assuming partition in-place
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if (inorder.length > 0) {
        var root = new TreeNode(preorder.shift());
        var index = inorder.indexOf(root.val);
        var right = inorder.splice(index + 1, inorder.length - index - 1);
        inorder.pop();
        root.left = buildTree(preorder, inorder);
        root.right = buildTree(preorder, right);
        return root;
    }
    return null;
};
