/* Given a list, rotate the list to the right by k places, 
 * where k is non-negative.
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
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (head === null)
        return null
    for (var count = 1, current = head; current.next; ++count)
        current = current.next
    current.next = head
    for (var i = 0; i < count - k % count; ++i)
        current = current.next
    head = current.next
    current.next = null
    return head
};
