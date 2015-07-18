# Given a binary search tree, write a function kthSmallest to find the kth 
# smallest element in it.
# Note: You may assume k is always valid, 1 <= k <= BST's total elements.
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
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        stack, node = [] if root else [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0: return node.val
                node = node.right

if __name__ == "__main__":
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.left = TreeNode(1)
    solution = Solution()
    print solution.kthSmallest(root, 2)
