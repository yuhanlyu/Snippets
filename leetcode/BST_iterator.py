# Implement an iterator over a binary search tree (BST). 
# Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# next() and hasNext() should run in average O(1) time and uses O(h) memory, 
# where h is the height of the tree.
# Time Complexity: O(n)
# Space Complexity: O(h), h is the height of the tree, O(1) is doable using
# Morris traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return node.val

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    it = BSTIterator(root)
    while it.hasNext():
        print it.next()
