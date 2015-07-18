# Given a binary tree, flatten it to a linked list in-place.
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
    def flatten(self, root):
        while root:
            if root.left:
                if root.right:
                    cur = root.left
                    while cur.right:
                        cur = cur.right
                    cur.right = root.right
                root.right, root.left = root.left, None
            root = root.right

if __name__ == "__main__":
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)
    solution = Solution()
    solution.flatten(node)
    print node.val, node.right.val, node.right.right.val
