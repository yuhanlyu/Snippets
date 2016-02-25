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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        dummy = ListNode(None, head)
        len, slow = 0, dummy
        while slow.next:
            len += 1
            slow = slow.next
        merge_size = 1
        while merge_size < len:
            run_start = dummy # node before two lists
            while run_start.next:
                second_list = first_list = pf = ps = slow = fast =run_start.next
                for _ in xrange(merge_size):
                    pf, slow = slow, slow.next
                    if not slow: break
                    if fast: ps, fast = fast, fast.next
                    if fast: ps, fast = fast, fast.next
                if not slow: break
                pf.next, ps.next, second_list = None, None, slow
                while first_list or second_list: # merge two lists
                    if (first_list and not second_list) or (first_list
                                  and first_list.val < second_list.val):
                        run_start.next, first_list = first_list, first_list.next
                    else:
                        run_start.next,second_list=second_list,second_list.next
                    run_start = run_start.next
                run_start.next = fast
            merge_size *= 2
        return dummy.next
