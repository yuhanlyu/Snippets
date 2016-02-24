class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        need, begin, end, cur, histogram, remain = {}, 0, len(source), 0, {}, len(target)
        for c in target:
            need[c] = need.get(c, 0) + 1
        for i, c in enumerate(source):
            if c in need:
                histogram[c] = histogram.get(c, 0) + 1
                if histogram[c] <= need[c]: remain -= 1
            while not remain:
                if  i - cur < end - begin: begin, end = cur, i
                if source[cur] in need:
                    histogram[source[cur]] -= 1
                    if histogram[source[cur]] < need[source[cur]]:
                        remain += 1
                cur += 1
        return source[begin:end + 1] if (end - begin) < len(source) else ""
