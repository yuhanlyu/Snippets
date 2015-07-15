# Sort a linked list using insertion sort.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        dummy, dummy.next = ListNode(None), head
        end = dummy.next
        while end and end.next:
            current = dummy
            while current.next.val < end.next.val:
                current = current.next
            if current != end:
                current.next, end.next.next, end.next = \
                end.next, current.next, end.next.next
            else:
                end = end.next
        return dummy.next

if __name__ == "__main__":
    list = head = ListNode(0)
    for i in xrange(5000):
        list.next = ListNode(i + 1)
        list = list.next
    solution = Solution()
    head = solution.insertionSortList(head)
    print "Solve"
    while head:
        print head.val
        head = head.next
