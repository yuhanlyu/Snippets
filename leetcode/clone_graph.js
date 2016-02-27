/* Clone an undirected graph. 
 * Each node in the graph contains a label and a list of its neighbors.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * Definition for undirected graph.
 * function UndirectedGraphNode(label) {
 *     this.label = label;
 *     this.neighbors = [];   // Array of UndirectedGraphNode
 * }
 */

/**
 * @param {UndirectedGraphNode} graph
 * @return {UndirectedGraphNode}
 */
var cloneGraph = function(graph) {
    function helper(node, map) {
        var new_node = new UndirectedGraphNode(node.label);
        map.set(node.label, new_node);
        for (var neighbor of node.neighbors) {
            if (!map.get(neighbor.label))
                map.set(neighbor.label, helper(neighbor, map));
            new_node.neighbors.push(map.get(neighbor.label));
        }
        return new_node;
    }
    return graph ? helper(graph, new Map()) : null;
};
