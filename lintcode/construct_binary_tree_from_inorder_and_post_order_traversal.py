"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if inorder:
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
            right, inorder[index:] = inorder[index + 1:], []
            post_right, postorder[index:] = postorder[index:], []
            root.left, root.right = self.buildTree(inorder, postorder), \
                                    self.buildTree(right, post_right)
            return root
