/* You are given an n x n 2D matrix representing an image.
 * Rotate the image by 90 degrees (clockwise).
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    var n = matrix[0].length;
    for (var i = 0; i < Math.floor(matrix[0].length / 2); ++i) {
        var bound = matrix[0].length - Math.floor(matrix[0].length / 2);
        for (var j = 0; j < bound; ++j) {
            var t1 = matrix[n-j-1][i];
            var t2 = matrix[n-i-1][n-j-1];
            var t3 = matrix[j][n-i-1];
            var t4 = matrix[i][j];
            matrix[i][j] = t1;
            matrix[n-j-1][i] = t2;
            matrix[n-i-1][n-j-1] = t3;
            matrix[j][n-i-1] = t4;
        }
    }
};
