"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution: 
    """
    @param root, index, value: The root of segment tree and 
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        if root.start == index == root.end: 
            root.max = value
        else:
            if index <= root.left.end:
                self.modify(root.left, index, value)
            else:
                self.modify(root.right, index, value)
            root.max = max(root.left.max, root.right.max)
