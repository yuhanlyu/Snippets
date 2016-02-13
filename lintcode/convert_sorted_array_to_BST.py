"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        def helper(A, begin, end):
            if begin == end: return None
            mid = begin + (end - begin) / 2
            root = TreeNode(A[mid])
            root.left, root.right = helper(A, begin, mid), \
                                    helper(A, mid + 1, end)
            return root
        return helper(A, 0, len(A))
