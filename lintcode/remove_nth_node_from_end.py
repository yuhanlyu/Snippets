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
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        nth = head
        for _ in xrange(n):
            nth = nth.next
        if not nth:
            return head.next
        current = head
        while nth.next:
            nth = nth.next
            current = current.next
        current.next = current.next.next
        return head
