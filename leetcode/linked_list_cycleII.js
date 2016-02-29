/* Given a linked list, return the node where the cycle begins. 
 * If there is no cycle, return null.
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
var detectCycle = function(head) {
    for (var slow = head, fast = head; fast; ) {
        slow = slow.next;
        fast = fast.next;
        if (!fast)
            break;
        fast = fast.next;
        if (slow === fast)
            break;
    }
    if (!fast)
        return null;
    while (head !== slow) {
        head = head.next;
        slow = slow.next;
    }
    return head;
};
