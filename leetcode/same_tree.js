/* Given two binary trees, write a function to check if they are equal or not.
 * Two binary trees are considered equal if they are structurally 
 * identical and the nodes have the same value.
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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (!p || !q)
        return !p && !q
    return (p.val == q.val) && isSameTree(p.left, q.left) 
                            && isSameTree(p.right, q.right)
};
