"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution: 
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalSum(self, A, queries):
        pre, cur, result = [0] * (len(A) + 1), 0, []
        for i, num in enumerate(A):
            cur += num
            pre[i + 1] = cur
        for query in queries:
            result.append(pre[query.end + 1] - pre[query.start])
        return result
