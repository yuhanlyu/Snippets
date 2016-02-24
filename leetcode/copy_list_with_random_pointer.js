/* A linked list is given such that each node contains an additional random 
 * pointer which could point to any node in the list or null.
 * Return a deep copy of the list.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * Definition for singly-linked list with a random pointer.
 * function RandomListNode(label) {
 *     this.label = label;
 *     this.next = this.random = null;
 * }
 */

/**
 * @param {RandomListNode} head
 * @return {RandomListNode}
 */
var copyRandomList = function(head) {
    if (!head)
        return null;
    for (var cur = head; cur; cur = next) {
        var next = cur.next;
        cur.next = new RandomListNode(cur.label);
        cur.next.next = next;
    }
    for (cur = head; cur; cur = cur.next.next) {
        if (cur.random)
            cur.next.random = cur.random.next;
    }
    var result = head.next;
    for (var cur1 = head, cur2 = head.next; cur1; cur1 = cur1.next, cur2 = cur2.next) {
        cur1.next = cur1.next.next;
        cur2.next = cur1.next ? cur2.next.next : null;
    }
    return result;
};
