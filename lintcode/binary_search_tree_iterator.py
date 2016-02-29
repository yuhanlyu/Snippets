"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.stack

    #@return: return next node
    def next(self):
        node = self.stack.pop()
        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return node
