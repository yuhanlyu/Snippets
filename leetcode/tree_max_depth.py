# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.
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
    # @return {integer}
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    solution = Solution()
    print solution.maxDepth(root)
