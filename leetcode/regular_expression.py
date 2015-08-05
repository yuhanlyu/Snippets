# Implement regular expression matching with support for '.' and '*'.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        def match(p, c, state, cache):
            if state == len(p): return []
            if p[state] == c or p[state] == '.':
                if state < len(p) - 1 and p[state + 1] == '*':
                    return epsilon(p, state, cache)
                return epsilon(p, state + 1, cache)
            return []
        def epsilon(p, state, cache):
            if state in cache: return cache[state]
            result = set([state])
            while state < len(p) - 1 and p[state + 1] == '*':
                state += 2
                result.add(state)
            cache[state] = result
            return result
        cache = {}
        states = epsilon(p, 0, cache)
        for c in s:
            states = set([x for y in states for x in match(p, c, y, cache)])
        return len(p) in states

if __name__ == "__main__":
    solution = Solution()
    print solution.isMatch("aa","a")
    print solution.isMatch("aa","aa")
    print solution.isMatch("aaa","aa")
    print solution.isMatch("aa", "a*")
    print solution.isMatch("aa", ".*")
    print solution.isMatch("ab", ".*")
    print solution.isMatch("aab", "c*a*b")
