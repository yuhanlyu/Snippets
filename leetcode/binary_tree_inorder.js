/* Given a binary tree, return the inorder traversal of its nodes' values.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    result = []
    node = root   
    while (node) {
        if (node.left) {
            for (pre = node.left; pre.right && pre.right !== node;)
                pre = pre.right
            if (pre.right) {
                result.push(node.val)
                node = node.right
                pre.right = null
            } else {
                pre.right = node
                node = node.left
            }
        } else {
            result.push(node.val)
            node = node.right
        }
    }
    return result
};

#class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
#    def inorderTraversal(self, root):
#        stack, result, node = [], [], root
#        while stack or node:
#            if node:
#                stack.append(node)
#                node = node.left
#            else:
#                node = stack.pop()
#                result.append(node.val)
#                node = node.right
#        return result
