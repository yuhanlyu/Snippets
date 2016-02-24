/* Given a set of candidate numbers (C) and a target number (T), find all 
 * unique combinations in C where the candidate numbers sums to T.
 * The same repeated number may be chosen from C unlimited number of times.
 * Time Complexity: O(n^n)
 * Space Complexity: O(n^n)
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    var DP = [];
    for (var i = 0; i <= target; ++i)
        DP.push([]);
    var temp = [];
    for (i = 0; i < candidates.length; ++i)
        if (candidates[i] <= target)
            temp.push(candidates[i]);
    temp.sort(function(a, b) { return a - b;});
    for (var candidate of temp) {
        DP[candidate].push([candidate]);
        for (i = candidate; i <= target; ++i) {
            for (var p of DP[i - candidate])
                DP[i].push(p.concat([candidate]));
        }
    }
    return DP[target];
};
