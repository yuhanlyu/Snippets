# Clone an undirected graph. 
# Each node in the graph contains a label and a list of its neighbors.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

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
                
if __name__ == "__main__":
    node1 = UndirectedGraphNode(1)
    node0 = UndirectedGraphNode(0)
    node2 = UndirectedGraphNode(2)
    node1.neighbors = [node0, node2]
    node0.neighbors = [node1, node2]
    node2.neighbors = [node0, node1, node2]
    solution = Solution()
    node = solution.cloneGraph(node0)
    print node.label
