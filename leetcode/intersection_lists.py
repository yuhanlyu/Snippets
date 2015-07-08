# Write a program to find the node at which the intersection of 
# two singly linked lists begins.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pa, pb = headA, headB
        while pa is not pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa

if __name__ == "__main__":
    a1 = ListNode("a1")
    a2 = ListNode("a2")
    b1 = ListNode("b1")
    b2 = ListNode("b2")
    b3 = ListNode("b3")
    c1 = ListNode("c1")
    c2 = ListNode("c2")
    c3 = ListNode("c3")

    a1.next = a2
    a2.next = c1
    b1.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = c3

    solution = Solution()
    print solution.getIntersectionNode(a1, b1).val
