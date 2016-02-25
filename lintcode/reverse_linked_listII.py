"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        dummy = ListNode(None)
        dummy.next, before = head, dummy
        for _ in xrange(m - 1):
            before = before.next
        begin, after = before.next, before.next.next
        for _ in xrange(n - m):
            begin.next, after.next, before.next = after.next, before.next, after
            after = begin.next
        return dummy.next
