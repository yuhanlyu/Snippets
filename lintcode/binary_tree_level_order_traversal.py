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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        def helper(root, level, levels):
            if root is not None:
                if len(levels) <= level:
                    levels.append([])
                levels[level].append(root.val)
                helper(root.left, level + 1, levels)
                helper(root.right, level + 1, levels)
            return levels
        return helper(root, 0, [])
