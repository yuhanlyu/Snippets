# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more 
# than 1.
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
    def isBalanced(self, root):
        def helper(root):
            if not root: return 0
            left_height = helper(root.left)
            if left_height < 0: return -2
            right_height = helper(root.right)
            if abs(left_height - right_height) > 1: return -2
            return 1 + max(left_height, right_height)
        return helper(root) >= 0

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    solution = Solution()
    print solution.isBalanced(root)
