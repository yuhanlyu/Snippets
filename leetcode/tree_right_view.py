# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
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
    # @return {integer[]}
    def rightSideView(self, root):
        def helper(root, level, result):
            if not root: return result
            if len(result) == level: result.append(root.val)
            helper(root.right, level + 1, result)
            helper(root.left, level + 1, result)
            return result
        return helper(root, 0, [])
                

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    solution = Solution()
    print solution.rightSideView(root)
