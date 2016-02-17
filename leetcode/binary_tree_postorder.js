/* Given a binary tree, return the postorder traversal of its nodes' values.
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
var postorderTraversal = function(root) {
    function reverse(begin, end) {
        for (cur = begin, next = begin.right; cur !== end; ) {
            temp = next.right
            next.right = cur
            cur = next
            next = temp
        }
    }
    result = []
    dummy = new TreeNode(0)
    dummy.left = root
    node = dummy
    while (node) {
        if (node.left){
            for (pre = node.left; pre.right && pre.right !== node; )
                pre = pre.right
            if (pre.right) {
                reverse(node.left, pre)
                for (cur = pre; ; cur = cur.right) {
                    result.push(cur.val)
                    if (cur == node.left)
                        break
                }
                reverse(pre, node.left)
                pre.right = null
                node = node.right
            } else {
                pre.right = node
                node = node.left
            }
        } else
            node = node.right
    }
    return result
};

#class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
#    def postorderTraversal(self, root):
#        stack, prev, result = [root] if root else [], root, []
#        while stack:
#            children = [x for x in (stack[-1].right, stack[-1].left) if x]
#            if not children or prev in children:
#                result.append(stack[-1].val)
#                prev = stack.pop()
#            else:
#                stack.extend(children)
#        return result
