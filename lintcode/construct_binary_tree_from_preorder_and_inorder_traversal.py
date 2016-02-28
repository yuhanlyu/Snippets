"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            right, inorder[index:] = inorder[index + 1:], []
            root.left, root.right = self.buildTree(preorder, inorder), \
                                    self.buildTree(preorder, right)
            return root
