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
        pre, result = [0], []
        for num in A:
            pre.append(pre[-1] + num)
        for query in queries:
            result.append(pre[query.end + 1] - pre[query.start])
        return result
