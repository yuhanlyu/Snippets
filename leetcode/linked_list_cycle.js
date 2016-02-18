/* Given a linked list, determine if it has a cycle in it.
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
 * @return {boolean}
 */
var hasCycle = function(head) {
    for (var slow = head, fast = head; fast; ) {
        slow = slow.next;
        fast = fast.next;
        if (!fast)
            break;
        fast = fast.next;
        if (slow === fast)
            return true;
    }
    return false;
};
