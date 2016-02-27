# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        indegree, result = dict.fromkeys(graph, 0), []
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        queue = deque([node for node, c in indegree.viewitems() if c == 0])
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return result
