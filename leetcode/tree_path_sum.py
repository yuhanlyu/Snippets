# Given a binary tree and a sum, determine if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals the given sum.
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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root: return False
        sum -= root.val
        if not root.left and not root.right and not sum: return True
        return self.hasPathSum(root.left, sum) \
            or self.hasPathSum(root.right, sum)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    solution = Solution()
    print solution.hasPathSum(root, 22)
