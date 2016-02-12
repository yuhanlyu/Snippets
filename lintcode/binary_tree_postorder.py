"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        def reverse(start, end):
            cur, next = start, start.right
            while cur != end:
                next.right, cur, next = cur, next, next.right
        result, dummy = [], TreeNode(None)
        dummy.left, node = root, dummy
        while node:
            if node.left:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                if pre.right:
                    reverse(node.left, pre)
                    cur = pre
                    while True:
                        result.append(cur.val)
                        if cur == node.left: break
                        cur = cur.right
                    reverse(pre, node.left)
                    node, pre.right = node.right, None
                else:
                    node, pre.right = node.left, node
            else:
                node = node.right
        return result
