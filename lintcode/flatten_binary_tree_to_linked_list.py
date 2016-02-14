"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        while root:
            if root.left:
                if root.right:
                    cur = root.left
                    while cur.right:
                        cur = cur.right
                    cur.right = root.right
                root.right, root.left = root.left, None
            root = root.right
