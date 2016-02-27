# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def helper(node, map):
            new = UndirectedGraphNode(node.label)
            map[node.label] = new
            for neighbor in node.neighbors:
                if neighbor.label not in map:
                    map[neighbor.label] = helper(neighbor, map)
                new.neighbors.append(map[neighbor.label])
            return new
        return helper(node, {}) if node else None
