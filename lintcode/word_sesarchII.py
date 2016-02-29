class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
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
