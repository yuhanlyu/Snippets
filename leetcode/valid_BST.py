# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the 
# node's key.
# The right subtree of a node contains only nodes with keys greater than the 
# node's key.
# Both the left and right subtrees must also be binary search trees.
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
    def isValidBST(self, root):
        stack, node, prev = [], root, None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev and prev.val >= node.val: return False
                prev = node 
                node = node.right
        return True

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    solution = Solution()
    print solution.isValidBST(root)
