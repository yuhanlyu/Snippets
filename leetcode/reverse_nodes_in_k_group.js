/* Given a linked list, reverse the nodes of a linked list k at a time and 
 * return its modified list.
 * If the number of nodes is not a multiple of k then left-out nodes in the end 
 * should remain as it is.
 * You may not alter the values in the nodes, only nodes itself may be changed.
 * Only constant memory is allowed.
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
var reverseKGroup = function(head, k) {
    var dummy = new ListNode(0);
    dummy.next = head;
    for (var cur = dummy; cur.next; ) {
        var g_head = cur;
        for (var i = 0; i < k && g_head.next; ++i)
            g_head = g_head.next;
        if (i !== k)
            break;
        var prev = g_head.next, next = g_head.next;
        for (g_head = cur.next; g_head !== next; ) {
            var t = g_head.next;
            g_head.next = prev;
            prev = g_head;
            g_head = t;
        }
        t = cur.next;
        cur.next = prev;
        cur = t;
    }
    return dummy.next;
};
