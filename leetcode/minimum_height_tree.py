# For a undirected graph with tree characteristics, we can choose any node as 
# the root. The result graph is then a rooted tree. Among all possible rooted 
# trees, those with minimum height are called minimum height trees (MHTs). 
# Given such a graph, write a function to find all the MHTs and return a list 
# of their root labels.
# Time Complexity: O(n)
# Space Complexity: O(n)

import collections

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: 
            return [0]
        neighbors = [set() for _ in xrange(n)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
        pre = [v for v in xrange(n) if len(neighbors[v]) == 1]
        while n > 2:
            n, next = n - len(pre), []
            for u in pre:
                v = neighbors[u].pop()
                neighbors[v].remove(u)
                if len(neighbors[v]) == 1:
                    next.append(v)
            pre = next
        return pre

if __name__ == "__main__":
    solution = Solution()
    print solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
    print solution.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], 
                                          [5, 4]])
