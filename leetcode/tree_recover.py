# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        node, previous, first, second = root, None, None, None
        while node:
            if node.left:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                if pre.right:
                    if previous and previous.val > node.val:
                        if not first: first = previous
                        second = node
                    previous = node
                    node, pre.right = node.right, None
                else:
                    pre.right, node = node, node.left
            else:
                if previous and previous.val > node.val:
                    if not first: first = previous
                    second = node
                previous = node
                node = node.right
        first.val, second.val = second.val, first.val

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    #root.left = TreeNode(3)
    solution = Solution()
    solution.recoverTree(root)
    print root.val, root.left.val
