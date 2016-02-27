/* Given an integer n, return all distinct solutions to the n-queens puzzle.
 * Each solution contains a distinct board configuration of the n-queens' 
 * placement, where 'Q' and '.' both indicate a queen and an empty space 
 * respectively.
 */

/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    var mx = new Array(n), d1 = new Array(2 * n), d2 = new Array(2 * n);
    mx.fill(false);
    d1.fill(false);
    d2.fill(false);
    var solution = new Array(n), temp = new Array(n), result = [];
    solution.fill(0);
    for (var stack = [[0, 0, false]]; stack.length > 0; ){
        var entry = stack.pop();
        var y = entry[0];
        var x = entry[1];
        if (entry[0] === n) {
            for (var board = new Array(n), i = 0; i < n; ++i) {
                temp.fill(".");
                temp[solution[i]] = "Q";
                board[i] = temp.join("");
            }
            result.push(board);
        } else if (!entry[2]) {
            if (x + 1 < n)
                stack.push([y, x + 1, false]);
            if (!mx[x] && !d1[x + y] && !d2[n - 1 + x - y]) {
                mx[x] = d1[x + y] = d2[n - 1 + x - y] = true;
                solution[y] = x;
                stack.push([y, x, true], [y + 1, 0, false]);
            }
        } else
            mx[x] = d1[x + y] = d2[n - 1 + x - y] = false;
    }
    return result;
};
