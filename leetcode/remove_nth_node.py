# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first 
# two lists.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        nth = head
        for _ in xrange(n - 1):
            nth = nth.next
        if not nth:
            return head.next
        current = head
        while nth.next:
            nth = nth.next
            current = current.next
        current.next = current.next.next
        return head


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    solution = Solution()
    list1 = solution.removeNthFromEnd(list1, 2)
    print list1.val, list1.next.val, list1.next.next
