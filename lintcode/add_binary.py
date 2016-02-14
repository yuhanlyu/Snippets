from collections import deque
class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        c, aindex, bindex = 0, len(a) - 1, len(b) - 1
        result = deque()
        while aindex >= 0 or bindex>= 0 or c:
            if aindex >= 0:
                c += int(a[aindex])
            if bindex >= 0:
                c += int(b[bindex])
            c, reminder = divmod(c, 2)
            result.appendleft(str(reminder))
            aindex -= 1
            bindex -= 1
        return ''.join(result)
