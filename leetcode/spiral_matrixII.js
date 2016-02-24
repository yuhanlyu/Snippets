/* Given an integer n, generate a square matrix filled with elements from 1 to 
 * n^2 in spiral order.
 * Time Complexity: O(n^2)
 * Space Complexity: O(n^2)
 */

/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    var d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    var result = [];
    for (var i = 0; i < n; ++i) {
        var tmp = new Array(n);
        tmp.fill(0);
        result.push(tmp);
    }
    var row = 0, column = 0, dir = 0;
    for (i = 1; i <= n * n; ++i) {
        result[row][column] = i;
        var nr = row + d[dir][0];
        var nc = column + d[dir][1];
        if (0 <= nr && nr < n && 0 <= nc && nc < n && result[nr][nc] === 0) {
            row = nr;
            column = nc;
        } else {
            dir = (dir + 1) % 4;
            row = row + d[dir][0];
            column = column + d[dir][1];
        }
    }
    return result;
};
