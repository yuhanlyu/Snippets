"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head is None: return None
        current = dummy = ListNode(None)
        current.next = head
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                v = current.next.val
                while current.next and current.next.val == v:
                    current.next = current.next.next
            else:
                current = current.next
        return dummy.next
