# Given preorder and inorder traversal of a tree, construct the binary tree.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            right, inorder[index:] = inorder[index + 1:], []
            root.left, root.right = self.buildTree(preorder, inorder), \
                                    self.buildTree(preorder, right)
            return root

if __name__ == "__main__":
    solution = Solution()
    node = solution.buildTree([1,2,3], [2, 1, 3])
    print node.val, node.left.val, node.right.val
    node = solution.buildTree([-1], [-1])
    print node.val
