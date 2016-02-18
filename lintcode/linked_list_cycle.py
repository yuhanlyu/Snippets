"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        slow = fast = head
        while fast:
            slow, fast = slow.next, fast.next
            if not fast: break
            fast = fast.next
            if slow == fast: return True
        return False
