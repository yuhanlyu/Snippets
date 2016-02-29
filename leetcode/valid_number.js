/* Validate if a given string is numeric.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    var state = 0, map = new Map([["+", 2], ["-", 2], ["E", 3], ["e", 3], [".", 4], [" ", 5]]);
    for (var c of "0123456789")
        map.set(c, 1);
    var transition = new Map();
    transition.set(0, new Map([[1, 5], [2, 3], [5, 0], [4, 2]]));
    transition.set(1, new Map([[1, 7], [2, 4]]));
    transition.set(2, new Map([[1, 6]]));
    transition.set(3, new Map([[1, 5], [4, 2]]));
    transition.set(4, new Map([[1, 7]]));
    transition.set(5, new Map([[1, 5], [3, 1], [4, 6], [5, 8]]));
    transition.set(6, new Map([[1, 6], [3, 1], [5, 8]]));
    transition.set(7, new Map([[1, 7], [5, 8]]));
    transition.set(8, new Map([[5, 8]]));
    for (c of s) {
        if (map.has(c) && transition.get(state).has(map.get(c)))
            state = transition.get(state).get(map.get(c));
        else
            return false;
    }
    return state >= 5;
};
