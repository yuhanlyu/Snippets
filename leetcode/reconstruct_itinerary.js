/* Given a list of airline tickets represented by pairs of departure and 
 * arrival airports [from, to], reconstruct the itinerary in order. All of the 
 * tickets belong to a man who departs from JFK. Thus, the itinerary must 
 * begin with JFK.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */


/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    var edges = new Map();
    tickets.sort();
    tickets.reverse();
    for (var entry of tickets) {
        if (!edges.has(entry[0]))
            edges.set(entry[0], []);
        edges.get(entry[0]).push(entry[1]);
    }
    for (var result = [], stack = ["JFK"]; stack.length > 0; ){
        while (edges.has(stack[stack.length - 1]) 
          && edges.get(stack[stack.length - 1]).length)
            stack.push(edges.get(stack[stack.length - 1]).pop());
        result.push(stack.pop());
    }
    result.reverse();
    return result;
};
