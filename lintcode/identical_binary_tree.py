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
        if not a and not b: return True
        if not a or not b: return False
        if a.val != b.val: return False
        return self.isIdentical(a.left, b.left) and \
               self.isIdentical(a.right, b.right)
