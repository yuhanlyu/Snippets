# Invert a binary tree.
# Time Complexity: O(n)
# Space Complexity: O(h), h is the height of the tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), \
                                    self.invertTree(root.left)
        return root
                
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    solution = Solution()
    root = solution.invertTree(root)
    print root.val, root.left.val, root.right.val
