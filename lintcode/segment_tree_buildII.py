"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution: 
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        def helper(start, end):
            if start > end: return None
            root = SegmentTreeNode(start, end, -1)
            if start == end:
                root.max = A[start]
            else:
                mid = start + (end - start) / 2
                root.left = helper(start, mid)
                root.right = helper(mid + 1, end)
                root.max = max(root.left.max, root.right.max)
            return root
        return helper(0, len(A) - 1)
