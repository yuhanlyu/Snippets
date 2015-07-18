# Given a binary tree, return the zigzag level order traversal of its nodes' 
# values. (ie, from left to right, then right to left for the next level and 
# alternate between).
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root: return []
        queue, result, level = deque([root, None]), [deque()], 0
        ops = [deque.append, deque.appendleft]
        while queue:
            node = queue.popleft()
            if not node:
                level += 1
                if queue: 
                    result.append(deque())
                    queue.append(None)
            else:
                ops[level % 2](result[level], node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return [list(item) for item in result]

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print solution.levelOrder(root)
