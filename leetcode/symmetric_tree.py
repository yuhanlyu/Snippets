# Given a binary tree, check whether it is a mirror of itself 
# (ie, symmetric around its center).
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
    # @return {boolean}
    def isSymmetric(self, root):
        def helper(root1, root2):
            if root1 is None or root2 is None:
                return root1 is None and root2 is None
            return root1.val == root2.val and helper(root1.left, root2.right) \
                                          and helper(root1.right, root2.left)
        return helper(root, root)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    solution = Solution()
    print solution.isSymmetric(root)
