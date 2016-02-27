/* Given a 2D binary matrix filled with 0's and 1's, find the largest square 
 * containing all 1's and return its area.
 * Time Complexity: O(mn)
 * Space Complexity: O(1)
 */

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    for (var result = 0, i = 0; i < matrix.length; ++i) {
        for (var j = 0; j < matrix[i].length; ++j) {
            matrix[i][j] = parseInt(matrix[i][j]);
            if (i > 0 && j > 0 && matrix[i][j] === 1)
                matrix[i][j] = 1 + Math.min(matrix[i-1][j-1], matrix[i][j-1], 
                                            matrix[i-1][j]);
            result = Math.max(result, matrix[i][j]);
        }
    }
    return result * result;
};
