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
        for start in xrange(len(words[0])):
            begin, histogram, remain = start, {}, len(words)
            for i in xrange(start, len(s) - len(words[0]) + 1, len(words[0])):
                str = s[i:i + len(words[0])]
                if str in need:
                    histogram[str] = histogram.get(str, 0) + 1
                    if histogram[str] <= need[str]: 
                        remain -= 1
                        if not remain:
                            result.append(begin)
                            histogram[s[begin:begin + len(words[0])]] -= 1
                            remain, begin = remain + 1, begin + len(words[0])
                    while histogram[str] > need[str]:
                        tmp = s[begin:begin + len(words[0])]
                        if histogram[tmp] <= need[tmp]: remain += 1
                        histogram[tmp] -= 1
                        begin += len(words[0])
                else:
                    remain, histogram, begin = len(words), {}, i + len(words[0])
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    #print solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
