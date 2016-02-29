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
    def intervalMinNumber(self, A, queries):
        M = [2 ** 32] * (len(A) * 4)
        def build(root, start, end):
            if start == end:
                M[root] = start
                return
            build(root * 2, start, start + (end - start) / 2)
            build(root * 2 + 1, start + (end - start) / 2 + 1, end)
            M[root] = M[root*2 + (0 if A[M[root*2]] <= A[M[root*2 + 1]] else 1)]
        def query(root, start, end, i, j):
            if i > end or j < start:
                return 2 ** 32
            if i <= start and end <= j:
                return A[M[root]]
            return min(query(root*2, start, start + (end - start)/2, i, j),
                       query(root*2 + 1, start+(end - start)/2 + 1, end, i, j))
        build(1, 0, len(A) - 1)
        return [query(1, 0, len(A) - 1, q.start, q.end) for q in queries]
