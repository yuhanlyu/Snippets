class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        def reverse(s, begin, end):
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1
        if len(s) > 0:
            offset %= len(s)
            reverse(s, 0, len(s) - 1)
            reverse(s, 0, offset - 1)
            reverse(s, offset, len(s) - 1)
