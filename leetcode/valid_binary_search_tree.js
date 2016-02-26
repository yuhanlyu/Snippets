/* Given a binary tree, determine if it is a valid binary search tree (BST).
 * Assume a BST is defined as follows:
 * The left subtree of a node contains only nodes with keys less than the 
 * node's key.
 * The right subtree of a node contains only nodes with keys greater than the 
 * node's key.
 * Both the left and right subtrees must also be binary search trees.
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
var isValidBST = function(root) {
    var stack = [];
    for (var node = root, prev = null; stack.length > 0 || node; ) {
        if (node) {
            stack.push(node);
            node = node.left;
        } else {
            node = stack.pop();
            if (prev && prev.val >= node.val)
                return false;
            prev = node;
            node = node.right;
        }
    }
    return true;
};
