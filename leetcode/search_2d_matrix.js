/* Write an efficient algorithm that searches for a value in an m x n matrix. 
 * This matrix has the following properties:
 * Integers in each row are sorted from left to right.
 * The first integer of each row is greater than the last integer of the 
 * previous row.
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    for (var left = 0, right = matrix.length - 1; left <= right; ) {
        var mid = left + Math.floor((right - left) / 2)
        if (matrix[mid][0] < target)
            left = mid + 1
        else
            right = mid - 1
    }
    if (left < matrix.length && matrix[left][0] === target)
        return true
    if (left === 0)
        return false
    var index = left - 1
    for (left = 0, right = matrix[index].length - 1; left <= right; ) {
        mid = left + Math.floor((right - left) / 2)
        if (matrix[index][mid] < target)
            left = mid + 1
        else
            right = mid - 1
    }
    return left < matrix[index].length && matrix[index][left] === target 
};
