/* Given an array of strings, group anagrams together.
 * Time Complexity: O(nm lg m), n is the number of strings, m is the length
 * Space Complexity: O(nm)
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    var d = new Map();
    for (var str of strs) {
        var list = str.split("");
        list.sort();
        var string = list.join("");
        if (!(d.get(string)))
            d.set(string, [])
        d.get(string).push(str);
    }
    var result = [];
    for (var entry of d) {
        entry[1].sort();
        result.push(entry[1]);
    }
    return result;
};
