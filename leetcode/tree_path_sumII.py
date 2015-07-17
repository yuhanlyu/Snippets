# Given a binary tree and a sum, find all root-to-leaf paths where each 
# path's sum equals the given sum.
# Time Complexity: O(n)
# Space Complexity: O(h + output), h is the height of the tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        def helper(root, path, goal, solution):
            if root:
                goal -= root.val
                path.append(root.val)
                if not root.left and not root.right and goal == 0:
                    solution.append(list(path))
                helper(root.left, path, goal, solution)
                helper(root.right, path, goal, solution)
                path.pop()
            return solution
        return helper(root, [], sum, [])

if __name__ == "__main__":
    root = TreeNode(1)
    solution = Solution()
    print solution.pathSum(root, 1)
