# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
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

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    head = solution.deleteDuplicates(head)
    print head.val, head.next.val, head.next.next.val
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    head = solution.deleteDuplicates(head)
    print head.val, head.next.val, head.next.next
