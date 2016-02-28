/* Given inorder and postorder traversal of a tree, construct the binary tree.
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
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    if (inorder.length > 0) {
        var root = new TreeNode(postorder.pop());
        var index = inorder.indexOf(root.val);
        var right = inorder.splice(index + 1, inorder.length - index - 1);
        inorder.pop();
        var post_right = postorder.splice(index, postorder.length - index);
        root.left = buildTree(inorder, postorder);
        root.right = buildTree(right, post_right);
        return root;
    }
    return null;
};
