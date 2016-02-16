/* Write an efficient algorithm that searches for a value in an m x n matrix. 
 * This matrix has the following properties:
 * Integers in each row are sorted in ascending from left to right.
 * Integers in each column are sorted in ascending from top to bottom.
 * Time Complexity: O(n + m)
 * Space Complexity: O(1)
 */

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    var row = 0, col = matrix[0].length - 1
    while (row < matrix.length && col >= 0) {
        if (matrix[row][col] == target)
            return true
        if (matrix[row][col] > target)
            --col
        else
            ++row
    }
    return false
};
