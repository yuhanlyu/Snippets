"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        def helper(head, count):
            if not count: return None, head
            (l, tail) = helper(head, count / 2)
            root = TreeNode(tail.val)
            (r, tail) = helper(tail.next, count - count / 2 - 1)
            root.left, root.right = l, r
            return root, tail
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next
        return helper(head, length)[0]
