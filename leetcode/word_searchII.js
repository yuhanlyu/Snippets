/* Given a 2D board and a list of words from the dictionary, find all words in 
 * the board.
 * Each word must be constructed from letters of sequentially adjacent cell, 
 * where "adjacent" cells are those horizontally or vertically neighboring. 
 * The same letter cell may not be used more than once in a word.
 */

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    function helper(board, trie, row, col, cur, result) {
        if (trie.get(null) === null) {
            trie.delete(null);
            result.push(cur.join(""));
        }
        if (!(0 <= row && row < board.length) 
         || !(0 <= col && col < board[row].length)
         || board[row][col] === null)
            return;
        if (!trie.get(board[row][col]))
            return;
        var c = board[row][col];
        board[row][col] = null;
        cur.push(c);
        for (var dir of [[1, 0], [-1, 0], [0, 1], [0, -1]])
            helper(board, trie.get(c), row + dir[0], col + dir[1], cur, result);
        cur.pop();
        board[row][col] = c;
    }
    var trie = new Map();
    for (var word of words) {
        var node = trie;
        for (var c of word) {
            if (!node.has(c))
                node.set(c, new Map());
            node = node.get(c);
        }
        node.set(null, null);
    }
    for (var result = [], i = 0; i < board.length; ++i) {
        for (var j = 0; j < board[i].length; ++j)
            helper(board, trie, i, j, [], result);
    }
    return result;
};
