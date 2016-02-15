/* Given a linked list, remove the nth node from the end of list and return 
 * its head.
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
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    for (var nth = head, i = 0; i < n; ++i)
        nth = nth.next
    if (!nth)
        return head.next
    for (var current = head; nth.next; nth = nth.next)
        current = current.next
    current.next = current.next.next
    return head
};
