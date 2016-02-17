/* Determine if a Sudoku is valid
 * Time Complexity: O(n^2)
 * Space Complexity: O(n), in this problem n is a constant
 */

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var row = [0, 0, 0, 0, 0, 0, 0, 0, 0]   
    var column = [0, 0, 0, 0, 0, 0, 0, 0, 0]   
    var block = [0, 0, 0, 0, 0, 0, 0, 0, 0]   
    for (var i = 0; i < board.length; ++i) {
        for (var j = 0; j < board[i].length; ++j) {
            if (board[i][j] !== '.') {
                mask = 1 << parseInt(board[i][j])
                blockIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3)
                if (mask & (row[i] | column[j] | block[blockIndex]))
                    return false
                row[i] |= mask
                column[j] |= mask
                block[blockIndex] |= mask
            }
        }
    }
    return true
};
