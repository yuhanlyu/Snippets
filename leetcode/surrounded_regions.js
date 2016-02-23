/* Given a 2D board containing 'X' and 'O', capture all regions surrounded by 
 * 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded 
 * region.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    if (board.length === 0)
        return;
    stack = [];
    for (var i = 0; i < board.length; ++i) {
        if (board[i][0] === 'O') {
            stack.push([i, 0]);
            board[i][0] = 'N';
        }
        if (board[i][board[0].length - 1] === 'O') {
            stack.push([i, board.length - 1]);
            board[i][board[0].length - 1] = 'N';
        }
    }
    for (var j = 0; j < board[0].length; ++j) {
        if (board[0][j] === 'O') {
            stack.push([0, j]);
            board[0][j] = 'N';
        }
        if (board[board.length - 1][j] === 'O') {
            stack.push([board.length - 1, j]);
            board[board.length - 1][j] = 'N';
        }
    }
    var directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    while (stack.length > 0) {
        var entry = stack.pop();
        var row = entry[0];
        var column = entry[1];
        for (i = 0; i < directions.length; ++i) {
            var newRow = row + directions[i][0];
            var newColumn = column + directions[i][1];
            if (0 <= newRow && newRow < board.length
             && 0 <= newColumn && newColumn < board[newRow].length
             && board[newRow][newColumn] === 'O') {
                board[newRow][newColumn] = 'N';
                stack.push([newRow, newColumn]);
            }
        }
    }
    for (i = 0; i < board.length; ++i) {
        for (j = 0; j < board[i].length; ++j) {
            if (board[i][j] === 'N')
                board[i][j] = 'O';
            else if (board[i][j] === 'O')
                board[i][j] = 'X';
        }
    }
};
