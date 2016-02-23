/* Given a m x n matrix, if an element is 0, set its entire row and column to 0.
 * Time complexity: O(mn)
 * Space complexity: O(1)
 */

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    var zeroInFirst = false;
    for (var i = 0; i < matrix.length; ++i) {
        if (matrix[i][0] === 0)
            zeroInFirst = true;
        for (var j = 1; j < matrix[i].length; ++j)
            if (matrix[i][j] === 0)
                matrix[i][0] = matrix[0][j] = 0;
    }
    for (i = matrix.length - 1; i >= 0; --i) {
        for (j = matrix[0].length - 1; j > 0; --j) {
            if (matrix[i][0] === 0 || matrix[0][j] === 0)
                matrix[i][j] = 0;
        }
        if (zeroInFirst)
            matrix[i][0] = 0;
    }
};
