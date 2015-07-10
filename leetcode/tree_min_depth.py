# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the 
# root node down to the nearest leaf node.
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
    def minDepth(self, root):
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    solution = Solution()
    print solution.minDepth(root)
