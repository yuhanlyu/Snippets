# You are given a string, s, and a list of words, words, that are all of the 
# same length. Find all starting indices of substring(s) in s that is a 
# concatenation of each word in words exactly once and without any intervening 
# characters.
# Time Complexity: O(n) in average, assuming each word has constant length
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        result, need = [], {}
        for word in words:
            need[word] = need.get(word, 0) + 1
        for i in xrange(len(words[0])):
            begin, remain = i, dict(need)
            for j in xrange(i, len(s) - len(words[0]) + 1, len(words[0])):
                str = s[j: j + len(words[0])]
                remain[str] = remain.get(str, 0) - 1
                while remain.get(str, -1) < 0:
                    remain[s[begin:begin + len(words[0])]] += 1
                    begin += len(words[0])
                if j + len(words[0]) - begin == len(words[0]) * len(words):
                    result.append(begin)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    #print solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
