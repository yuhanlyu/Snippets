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
    @return: nothing
    """
    def reorderList(self, head):
        if not head: return head
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow, prev = None, slow.next, None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next
        while head and prev:
            prev.next,prev,head.next,head = head.next,prev.next,prev,head.next
