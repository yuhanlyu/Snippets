# Given a binary tree, return the preorder traversal of its nodes' values.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        stack, result = [root] if root else [], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    solution = Solution()
    print solution.preorderTraversal(root)
