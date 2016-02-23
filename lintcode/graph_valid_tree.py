class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        def helper(parent, root):
            if root in visited: return False
            visited.add(root)
            for neighbor in graph.get(root, []):
                if neighbor != parent and not helper(root, neighbor):
                    return False
            return True
        graph = {}
        for edge in edges:
            graph.setdefault(edge[0], set()).add(edge[1])
            graph.setdefault(edge[1], set()).add(edge[0])
        visited = set()
        return helper(0, 0) and len(visited) == n
