"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        def isSame(T1, T2):
            if not T1 and not T2: return True
            if not T1 or not T2: return False
            if T1.val != T2.val: return False
            return isSame(T1.left, T2.left) and isSame(T1.right, T2.right)
        if not T2: return True
        if not T1: return False
        return isSame(T1, T2) or self.isSubtree(T1.left, T2) \
                              or self.isSubtree(T1.right, T2)
            
