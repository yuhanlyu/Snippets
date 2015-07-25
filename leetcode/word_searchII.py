# Given a 2D board and a list of words from the dictionary, find all words in 
# the board.
# Each word must be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        def helper(board, trie, row, col, cur, result):
            if trie.pop(None, False): result.append(''.join(cur))
            if row < 0 or row >= len(board) \
            or col < 0 or col >= len(board[row]) or not board[row][col]: 
                return
            if board[row][col] not in trie: return 
            c = board[row][col]
            board[row][col] = None
            cur.append(c)
            for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                helper(board, trie[c], row + drow, col + dcol, cur, result)
            cur.pop()
            board[row][col] = c
        trie, result = {}, []
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                helper(board, trie, i, j, [], result)
        return result

if __name__ == "__main__":
    solution = Solution()
    board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
    print solution.findWords(board, ["oath","pea","eat","rain"])
