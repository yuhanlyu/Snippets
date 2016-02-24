/* Given a binary tree, return the zigzag level order traversal of its nodes' 
 * values. (ie, from left to right, then right to left for the next level and 
 * alternate between).
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
var zigzagLevelOrder = function(root) {
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
    for (var i = 1; i < result.length; i += 2)
        result[i].reverse();
    return result;
};
