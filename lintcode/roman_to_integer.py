class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
        map = [0] * 256
        map[ord('M')], map[ord('D')], map[ord('C')] = 1000, 500, 100
        map[ord('L')], map[ord('X')], map[ord('V')] = 50, 10, 5
        map[ord('I')] = 1
        previous = result = map[ord(s[-1])]
        for index in xrange(len(s) - 2, -1, -1):
            val = map[ord(s[index])]
            result += val if val >= previous else -val
            previous = val
        return result
