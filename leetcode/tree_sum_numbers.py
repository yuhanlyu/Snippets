# Given a binary tree containing digits from 0-9 only, 
# each root-to-leaf path could represent a number.
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
    def sumNumbers(self, root):
        def helper(root, num):
            if not root: return 0
            if not root.left and not root.right: return num + root.val
            return helper(root.left, (num + root.val) * 10) \
                 + helper(root.right, (num + root.val) * 10)
            return result
        return helper(root, 0)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print solution.sumNumbers(root)
