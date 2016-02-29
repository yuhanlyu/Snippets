/* Given a collection of candidate numbers (C) and a target number (T), 
 * find all unique combinations in C where the candidate numbers sums to T.
 * Each number in C may only be used once in the combination.
 * Time Complexity: O(n^n)
 * Space Complexity: O(n^n)
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    var DP = [], cnt = new Map(), temp = [];
    for (var i = 0; i <= target; ++i)
        DP.push([]);
    for (var candidate of candidates) {
        if (candidate <= target) {
            if (!cnt.has(candidate)) {
                cnt.set(candidate, 0);
                temp.push(candidate);
            }
            cnt.set(candidate, cnt.get(candidate) + 1);
        }
    }
    temp.sort(function(a, b) { return a - b; });
    for (candidate of temp) {
        for (var t = 1; t <= cnt.get(candidate); ++t) {
            if (t * candidate > target)
                break;
            var list = new Array(t);
            list.fill(candidate);
            DP[t * candidate].push(list);
            for (i = target; i >= t * candidate; --i) {
                for (var p of DP[i - t * candidate]) {
                    if (p[p.length - 1] !== candidate) {
                        DP[i].push(p.concat(list));
                    }
                }
            }
        }
    }
    return DP[target];
};
