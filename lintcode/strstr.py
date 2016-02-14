class Solution:
    def strStr(self, source, target):
        if target == "": return 0
        if not source or not target: return -1
        failure = [-1] * (len(target) + 1)
        for index in xrange(1, len(target) + 1):
            pos = failure[index - 1]
            while pos != -1 and target[pos] != target[index - 1]:
                pos = failure[pos]
            failure[index] = pos + 1
        ti, pi = 0, 0
        for ti in xrange(len(source)):
            while pi != -1 and source[ti] != target[pi]:
                pi = failure[pi]
            pi += 1
            if pi == len(target):
                return ti + 1 - len(target)
        return -1
