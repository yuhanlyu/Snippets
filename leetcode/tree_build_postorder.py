# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    def buildTree(self, inorder, postorder):
        if inorder:
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
            right, inorder[index:] = inorder[index + 1:], []
            post_right, postorder[index:] = postorder[index:], []
            root.left, root.right = self.buildTree(inorder, postorder), \
                                    self.buildTree(right, post_right)
            return root

if __name__ == "__main__":
    solution = Solution()
    node = solution.buildTree([2, 1, 3], [2, 3, 1])
    print node.val, node.left.val, node.right.val
