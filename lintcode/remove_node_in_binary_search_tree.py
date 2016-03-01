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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        def find_min(root):
            while root and root.left:
                root = root.left
            return root
        def delete_min(root):
            if not root.left:
                return root.right
            node, p = root, None
            while node and node.left:
                p, node = node, node.left
            p.left = node.right
            return root
        if not root:
            return None
        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            root, t = find_min(root.right), root
            root.right, root.left = delete_min(t.right), t.left
        return root
