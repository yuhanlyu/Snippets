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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        slow = fast = head
        while fast:
            slow, fast = slow.next, fast.next
            if not fast: break
            fast = fast.next
            if slow == fast: break
        if not fast: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
