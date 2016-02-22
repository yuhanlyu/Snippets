/* Given an absolute path for a file (Unix-style), simplify it.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    var result = []
    for (var str of path.split("/")) {
        if (str.length === 0)
            continue;
        if (str === "..") {
            if (result.length > 0) {
                result.pop();
            }
        } else if (str !== ".") {
            result.push(str);
        }
    }
    return "/".concat(result.join("/"));
};
