# Given a binary tree, return all root-to-leaf paths.
# Time Complexity: O(n + output)
# Space Complexity: O(h + output)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def helper(root, path, result):
            if not root.left and not root.right:
                result.append("->".join(path + [str(root.val)]))
            else:
                if root.left: helper(root.left, path + [str(root.val)], result)
                if root.right: helper(root.right, path+[str(root.val)], result)
            return result
        return helper(root, [], []) if root else []

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    solution = Solution()
    print solution.binaryTreePaths(root)
