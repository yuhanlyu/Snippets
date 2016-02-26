from collections import deque
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = deque([(start, 1)])
        dict.add(end)
        while queue:
            str, length = queue.popleft()
            for new in (str[:i] + c + str[i + 1:]
                        for i in xrange(len(str))
                        for c in "abcdefghijklmnopqrstuvwxyz"
                        if c != str[i] and str[:i]+c+str[i+1:] in dict):
                    if new == end: return length + 1
                    queue.append((new, length + 1))
                    dict.remove(new)
        return 0
