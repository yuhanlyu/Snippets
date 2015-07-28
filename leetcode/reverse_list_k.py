# Given a linked list, reverse the nodes of a linked list k at a time and 
# return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end 
# should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        cur = dummy = ListNode(0)
        dummy.next = head
        while cur.next:
            g_head, i = cur, 0
            while i < k:
                if g_head.next: g_head, i = g_head.next, i + 1
                else: break
            if i != k: break
            g_head, prev, next = cur.next, g_head.next, g_head.next
            while g_head != next:
                prev, g_head.next, g_head = g_head, prev, g_head.next
            cur.next, cur = prev, cur.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    solution = Solution()
    head = solution.reverseKGroup(head, 3)
    print head.val, head.next.val, head.next.next.val, head.next.next.next.val
