/* Sort a linked list using insertion sort.
 * Time Complexity: O(n^2)
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
var insertionSortList = function(head) {
    dummy = new ListNode(0)
    dummy.next = head
    pre = dummy
    cur = head
    while (cur) {
        if (cur.next && cur.next.val < cur.val) {
            while (pre.next && pre.next.val < cur.next.val)
                pre = pre.next
            temp = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = temp
            pre = dummy
        } else {
            cur = cur.next
        }
    }
    return dummy.next
};
