/* Given a binary tree, return all root-to-leaf paths.
 * Time Complexity: O(n + output)
 * Space Complexity: O(h + output)
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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    function helper(root, path, result) {
        if (!root.left && !root.right)
            result.push(path.concat(root.val.toString()).join("->"))
        else {
            if (root.left)
                helper(root.left, path.concat(root.val.toString()), result)
            if (root.right)
                helper(root.right, path.concat(root.val.toString()), result)
        }
        return result
    }
    return root ? helper(root, [], []) : []
};
