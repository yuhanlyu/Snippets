/* Given a binary tree, flatten it to a linked list in-place.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    for (; root; root = root.right) {
        if (root.left) {
            if (root.right) {
                for (cur = root.left; cur.right; )
                    cur = cur.right
                cur.right = root.right
            }
            root.right = root.left
            root.left = null
        }
    }
}
