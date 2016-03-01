/* Given an integer matrix, find the length of the longest increasing path.
 * From each cell, you can either move to four directions: left, right, up or 
 * down. You may NOT move diagonally or move outside of the boundary (i.e. 
 * wrap-around is not allowed).
 * Time Complexity: O(n^2)
 * Space Complexity: O(n^2)
 */


/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    function helper(row, col) {
        if (DP[row][col] === 0) {
            var result = 1;
            for (var dir of [[0, 1], [0, -1], [1, 0], [-1, 0]]) {
                var new_row = row + dir[0], new_col = col + dir[1];
                if (!(0 <= new_row && new_row < matrix.length) 
                 || !(0 <= new_col && new_col < matrix[new_row].length))
                     continue;
                if (matrix[new_row][new_col] > matrix[row][col])
                    result = Math.max(result, 1 + helper(new_row, new_col));
            }
            DP[row][col] = result;
        }
        return DP[row][col];
    }
    var DP = [];
    for (var row of matrix) {
        var temp = new Array(row.length);
        temp.fill(0);
        DP.push(temp);
    }
    for (var result = 0, i = 0; i < matrix.length; ++i)
        for (var j = 0; j < matrix[i].length; ++j)
            result = Math.max(result, helper(i, j));
    return result;
};
