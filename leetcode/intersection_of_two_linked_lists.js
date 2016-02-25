/* Write a program to find the node at which the intersection of 
 * two singly linked lists begins.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    for (var pa = headA, pb = headB; pa != pb;) {
        pa = pa ? pa.next : headB;
        pb = pb ? pb.next : headA;
    }
    return pa;
};
