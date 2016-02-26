"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        def helper(root, result):
            if not root:
                return result
            if k1 < root.val:
                helper(root.left, result)
            if k1 <= root.val <= k2:
                result.append(root.val)
            if k2 > root.val:
                helper(root.right, result)
            return result
        return helper(root, []);
