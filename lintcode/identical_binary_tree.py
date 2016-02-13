"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        if not a or not b:
            return not a and not b
        return a.val == b.val and self.isIdentical(a.left, b.left) \
                              and self.isIdentical(a.right, b.right)
