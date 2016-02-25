# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        pa, pb = headA, headB
        while pa is not pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa
