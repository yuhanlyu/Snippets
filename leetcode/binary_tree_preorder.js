/* Given a binary tree, return the preorder traversal of its nodes' values.
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
var preorderTraversal = function(root) {
    result = []
    node = root
    while (node) {
        if (node.left) {
            for (pre = node.left; pre.right && pre.right != node; )
                pre = pre.right
            if (pre.right) {
                node = node.right
                pre.right = null
            } else {
                result.push(node.val)
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
#    def preorderTraversal(self, root):
#        stack, result = [root] if root else [], []
#        while stack:
#            node = stack.pop()
#            result.append(node.val)
#            if node.right: stack.append(node.right)
#            if node.left: stack.append(node.left)
#        return result
