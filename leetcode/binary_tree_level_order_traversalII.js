/* Given a binary tree, return the bottom-up level order traversal of its 
 * nodes' values. (ie, from left to right, level by level from leaf to root).
 * Time Complexity: O(n)
 * Space Complexity: O(n)
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
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    function helper(root, level, levels) {
        if (root) {
            if (levels.length <= level)
                levels.push([]);
            levels[level].push(root.val);
            helper(root.left, level + 1, levels);
            helper(root.right, level + 1, levels);
        }
        return levels;
    }
    var result = helper(root, 0, []);
    result.reverse();
    return result;
};
