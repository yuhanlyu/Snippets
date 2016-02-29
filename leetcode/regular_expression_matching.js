/* Implement regular expression matching with support for '.' and '*'.
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    function match(p, c, state, cache) {
        if (state === p.length)
            return [];
        if (p.charAt(state) === c || p.charAt(state) === '.') {
            if (state < p.length - 1 && p.charAt(state + 1) === '*')
                return epsilon(p, state, cache);
            return epsilon(p, state + 1, cache);
        }
        return [];
    }
    function epsilon(p, state, cache) {
        if (cache.has(state))
            return cache.get(state);
        var result = new Set([state]);
        while (state < p.length - 1 && p.charAt(state + 1) === '*') {
            state += 2;
            result.add(state);
        }
        cache.set(state, result);
        return result;
    }
    var cache = new Map();
    var states = epsilon(p, 0, cache);
    for (var c of s) {
        var temp = new Set();
        for (var y of states) {
            for (var x of match(p, c, y, cache))
                temp.add(x);
        }
        states = temp;
    }
    return states.has(p.length);
};
