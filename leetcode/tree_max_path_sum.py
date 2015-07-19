# Given a binary tree, find the maximum path sum.  
# The path may start and end at any node in the tree.
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
    def maxPathSum(self, root):
        def helper(root):
            if not root: return (None, 0)
            (l_max, l) = helper(root.left)
            (r_max, r) = helper(root.right)
            return (max(filter(lambda x: x is not None, [l_max, r_max, 
                    l + r + root.val])), max(max(l, r) + root.val, 0))
        return helper(root)[0]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print solution.maxPathSum(root)
