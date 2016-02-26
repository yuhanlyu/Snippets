/* Given a 2D board and a word, find if the word exists in the grid.
 * The word can be constructed from letters of sequentially adjacent cell, 
 * where "adjacent" cells are those horizontally or vertically neighboring. 
 * The same letter cell may not be used more than once.
 */

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    function helper(row, col, visited, word, level) {
        if (row < 0 || row >= board.length
         || col < 0 || col >= board[row].length
         || visited[row][col] === true || board[row][col] !== word.charAt(level))
            return false;
        if (level === word.length - 1)
            return true;
        visited[row][col] = true;
        for (var dir of [[0, 1], [0, -1], [1, 0], [-1, 0]]) {
            if (helper(row + dir[0], col + dir[1], visited, word, level + 1))
                return true;
        }
        visited[row][col] = false;
        return false;
    }
    var visited = new Array(board.length);
    for (var i = 0; i < board.length; ++i) {
        var temp = new Array(board[i].length);
        temp.fill(false);
        visited[i] = temp;
    }
    for (i = 0; i < board.length; ++i) {
        for (var j = 0; j < board[i].length; ++j)
            if (helper(i, j, visited, word, 0))
                return true;
    }
    return false;
};
