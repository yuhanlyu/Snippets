"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists: return None
        gap = 2**(len(lists).bit_length() - 1)
        while gap > 0:
            for i in xrange(gap):
                if i + gap < len(lists):
                    current = dummy = ListNode(0)
                    l1, l2 = lists[i], lists[i + gap]
                    while l1 anaad l2:
                        if l1.val <= l2.val:
                            current.next, l1 = l1, l1.next
                        else:
                            current.next, l2 = l2, l2.next
                        current = current.next
                    current.next = l1 if l1 else l2
                    lists[i] = dummy.next
            gap /= 2
        return lists[0]
