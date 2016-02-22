/* Given n pairs of parentheses, write a function to generate all combinations 
 * of well-formed parentheses.
 * Time Complexity: O(4^n)
 * Space Complexity: O(4^n)
 */

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var cur = new Array(2 * n + 1);
    for (var i = 0; i < cur.length; ++i)
        cur[i] = i <= n ? "(" : ")";
    var result = [], x = n, y = n;
    while (true) {
        result.push(cur.slice(1).join(""));
        if (x >= 2 * n - 1)
            break;
        cur[x++] = ")";
        cur[y++] = "(";
        if (cur[x] === ")") {
            if (x === 2 * y - 2)
                ++x;
            else {
                cur[x] = "(";
                cur[2] = ")";
                x = 3;
                y = 2;
            }
        }
    }
    return result;
};
