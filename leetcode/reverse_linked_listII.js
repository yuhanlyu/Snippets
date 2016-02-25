/* Reverse a linked list from position m to n. Do it in-place and in one-pass.
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
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
    var dummy = new ListNode(null), before = dummy;
    dummy.next = head;
    for (var i = 0; i < m - 1; ++i)
        before = before.next;
    var begin = before.next, after = before.next.next;
    for (i = 0; i < n - m; ++i) {
        begin.next = after.next;
        after.next = before.next;
        before.next = after;
        after = begin.next;
    }
    return dummy.next;
};
