# Given two words (beginWord and endWord), and a dictionary, find the length 
# of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        words, queue = set(wordDict), deque([(beginWord, 1)])
        while queue:
            str, length = queue.popleft()
            for i in xrange(len(str)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == str[i]: continue
                    new_str = str[:i] + c + str[i + 1:]
                    if new_str == endWord: return length + 1
                    if new_str in words:
                        queue.append((new_str, length + 1))
                        words.remove(new_str)
        return 0

if __name__ == "__main__":
    solution = Solution()
    print solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
