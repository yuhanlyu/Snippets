/* Given a binary tree, return the level order traversal of its nodes' values. 
 * (ie, from left to right, level by level).
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
var levelOrder = function(root) {
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
    return helper(root, 0, []);
};
