"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
class Solution:
    """
    @param root: The root of binary tree.
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue, result, level = deque([root, None] if root else []), [deque()], 0
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
