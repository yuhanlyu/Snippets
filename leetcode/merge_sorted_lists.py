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
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(2)
    list2 = ListNode(1)
    list2.next = ListNode(1)
    list2.next.next = ListNode(2)
    list2.next.next.next = ListNode(3)
    list2.next.next.next.next = ListNode(3)
    solution = Solution()
    list1 = solution.mergeTwoLists(list1, list2)
    print list1.val, list1.next.val, list1.next.next.val
