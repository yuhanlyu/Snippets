/* Sort a linked list in O(n log n) time using constant space complexity.
 * Time Complexity: O(n lg n)
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
var sortList = function(head) {
    var dummy = new ListNode(null);
    dummy.next = head;
    for (var len = 0, slow = dummy; slow.next; ++len)
        slow = slow.next;
    for (var merge_size = 1; merge_size < len; merge_size *= 2) {
        for (var run_start = dummy; run_start.next; ) {
            var pf = run_start.next, ps = run_start.next;
            slow = run_start.next;
            for (var fast = run_start.next, i = 0; i < merge_size; ++i) {
                pf = slow;
                slow = slow.next;
                if (!slow)
                    break;
                if (fast) {
                    ps = fast;
                    fast = fast.next;
                }
                if (fast) {
                    ps = fast;
                    fast = fast.next;
                }
            }
            if (!slow)
                break;
            pf.next = null;
            ps.next = null;
            var first_list = run_start.next, second_list = slow;
            for (; first_list || second_list; run_start = run_start.next) {
                if ((first_list && !second_list)
                 || (first_list && first_list.val < second_list.val)) {
                     var temp = first_list.next;
                     run_start.next = first_list;
                     first_list = temp;
                 } else {
                     temp = second_list.next;
                     run_start.next = second_list;
                     second_list = temp;
                 }
            }
            run_start.next = fast;
        }
    }
    return dummy.next;
};
