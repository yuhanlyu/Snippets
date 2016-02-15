"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        tail = greater = ListNode(None)
        previous = dummy = ListNode(None)
        current = dummy.next = head
        while current:
            if current.val >= x:
                tail.next, tail = current, current
                previous.next = current.next
            else:
                previous = current
            current = current.next
        tail.next = None
        previous.next = greater.next
        return dummy.next
