class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        queue, parent, level = [set([start]), set()], {}, False
        dict.add(end)
        while queue[level] and end not in parent:
            new_parent, queue[not level] = {}, set()
            for str, new in ((str, str[:i] + c + str[i + 1:])
                        for str in queue[level]
                        for c in "abcdefghijklmnopqrstuvwxyz"
                        for i in xrange(len(str))
                        if c != str[i] and str[:i] + c + str[i + 1:] in dict
                                and str[:i] + c + str[i + 1:] not in parent):
                new_parent.setdefault(new, []).append(str)
                queue[not level].add(new)
            parent.update(new_parent)
            level = not level
        result = [[end]]
        while result and result[0][0] != start:
            result = [[p] + c for c in result for p in parent.get(c[0], [])]
        return result
