# Given a complete binary tree, count the number of nodes.
# Time Complexity: O(lg^2 n)
# Space Complexity: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        def height(root):
            count = 0
            while root:
                root = root.left
                count += 1
            return count
        nodes, root_height = 0, height(root)
        while root:
            right_height = height(root.right)
            nodes += 2 ** (right_height)
            root_height -= 1
            root = root.right if root_height == right_height else root.left
        return nodes

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    solution = Solution()
    print solution.countNodes(root)
