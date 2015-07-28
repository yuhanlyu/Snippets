# Merge k sorted linked lists and return it as one sorted list. 
# Analyze and describe its complexity.
# Time Complexity: O(n lg k)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists: return None
        gap = 2**(len(lists).bit_length() - 1)
        while gap > 0:
            for i in xrange(gap):
                if i + gap < len(lists):
                    current = dummy = ListNode(0)
                    l1, l2 = lists[i], lists[i + gap]
                    while l1 and l2:
                        if l1.val <= l2.val:
                            current.next, l1 = l1, l1.next
                        else:
                            current.next, l2 = l2, l2.next
                        current = current.next
                    current.next = l1 if l1 else l2
                    lists[i] = dummy.next
            gap /= 2
        return lists[0]

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
    list1 = solution.mergeKLists([list1, list2])
    print list1.val, list1.next.val, list1.next.next.val
