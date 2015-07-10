# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
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
    # @return {integer[][]}
    def levelOrder(self, root):
        def helper(root, level, levels):
            if root is not None:
                if len(levels) <= level:
                    levels.append([])
                levels[level].append(root.val)
                helper(root.left, level + 1, levels)
                helper(root.right, level + 1, levels)
            return levels
        return helper(root, 0, [])

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print solution.levelOrder(root)
