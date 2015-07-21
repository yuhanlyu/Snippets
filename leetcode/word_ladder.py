# Given two words (beginWord and endWord), and a dictionary, find the length 
# of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# Time Complexity: O(n 26^l), l is the length of each word
# Space Complexity: O(n)

from collections import deque

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        queue = deque([(beginWord, 1)])
        wordDict.add(endWord)
        while queue:
            str, length = queue.popleft()
            for i in xrange(len(str)):
                for new in (str[:i] + c + str[i + 1:] 
                            for c in "abcdefghijklmnopqrstuvwxyz" 
                            if c != str[i] and str[:i]+c+str[i+1:] in wordDict):
                    if new == endWord: return length + 1
                    queue.append((new, length + 1))
                    wordDict.remove(new)
        return 0

if __name__ == "__main__":
    solution = Solution()
    print solution.ladderLength("hit", "cog", 
                                set(["hot","dot","dog","lot","log"]))
