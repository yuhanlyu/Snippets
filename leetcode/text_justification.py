# Given an array of words and a length L, format the text such that each line 
# has exactly L characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words 
# as you can in each line. Pad extra spaces ' ' when necessary so that each 
# line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible. If 
# the number of spaces on a line do not divide evenly between words, the empty 
# slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is 
# inserted between words.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        result, cur, length = [], [], 0
        for word in words:
            if length + len(word) + len(cur) > maxWidth:
                if len(cur) == 1: result.append("%-*s" % (maxWidth, cur[0]))
                else:
                    space, remain = divmod(maxWidth - length, len(cur) - 1)
                    result.append(''.join([cur[0]] + \
                                 ["%*s" % (space + (i < remain) + len(x), x) \
                                           for (i, x) in enumerate(cur[1:])]))
                length, cur = 0, []
            cur.append(word)
            length += len(word)
        if len(cur) >= 1: result.append("%-*s" % (maxWidth, ' '.join(cur)))
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
