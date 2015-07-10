# Given two binary trees, write a function to check if they are equal or not.
# Two binary trees are considered equal if they are structurally 
# identical and the nodes have the same value.
# Time Complexity: O(n)
# Space Complexity: O(h), h is the height of the tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p is None or q is None:
            return p is None and q is None
        return p.val == q.val and self.isSameTree(p.left, q.left) \
                              and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    solution = Solution()
    print solution.isSameTree(root, root)
