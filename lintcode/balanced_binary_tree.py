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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        def helper(root):
            if not root: return 0
            left_height = helper(root.left)
            if left_height < 0: return -2
            right_height = helper(root.right)
            if abs(left_height - right_height) > 1: return -2
            return 1 + max(left_height, right_height)
        return helper(root) >= 0
