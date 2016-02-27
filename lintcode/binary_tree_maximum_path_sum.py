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
    @return: An integer
    """
    def maxPathSum(self, root):
        def helper(root):
            if not root: return (None, 0)
            (l_max, l) = helper(root.left)
            (r_max, r) = helper(root.right)
            return (max(filter(lambda x: x is not None, [l_max, r_max, 
                    l + r + root.val])), max(max(l, r) + root.val, 0))
        return helper(root)[0]
