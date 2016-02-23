/* Given a matrix of m x n elements (m rows, n columns), return all elements of 
 * the matrix in spiral order.
 * Time Complexity: O(mn)
 * Space Complexity: O(mn)
 */

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if (matrix.length === 0)
        return [];
    var d = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    var remain = [matrix[0].length, matrix.length - 1];
    var result = [];
    for (var row = 0, column = -1, dir = 0; remain[dir % 2] > 0; ) {
        for (var i = 1; i < remain[dir % 2] + 1; ++i)
            result.push(matrix[row + i * d[dir][0]][column + i * d[dir][1]]);
        row += d[dir][0] * remain[dir % 2];
        column += d[dir][1] * remain[dir % 2];
        --remain[dir % 2];
        dir = (dir + 1) % 4;
    }
    return result;
};
