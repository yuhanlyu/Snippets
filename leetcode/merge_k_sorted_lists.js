/* Merge k sorted linked lists and return it as one sorted list. 
 * Analyze and describe its complexity.
 * Time Complexity: O(n lg k)
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
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if (lists.length === 0)
        return [];
    for (var gap = 1; gap * 2 < lists.length; gap *= 2)
        ;
    for (; gap > 0; gap = Math.floor(gap / 2)) {
        for (var i = 0; i < gap; ++i) {
            if (i + gap >= lists.length)
                continue;
            var dummy = new ListNode(0);
            var l1 = lists[i], l2 = lists[i + gap];
            for (var current = dummy; l1 && l2; current = current.next) {
                if (l1.val <= l2.val) {
                    current.next = l1;
                    l1 = l1.next;
                } else {
                    current.next = l2;
                    l2 = l2.next;
                }
            }
            current.next = l1 ? l1 : l2;
            lists[i] = dummy.next;
        }
    }
    return lists[0];
};
