/* Given a linked list, swap every two adjacent nodes and return its head.
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
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    current = dummy = new ListNode(0)
    dummy.next = head
    for (; current.next && current.next.next; current = current.next.next) {
        first = current.next
        second = current.next.next
        current.next = second
        first.next = second.next
        second.next = first
    }
    return dummy.next
};
