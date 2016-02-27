class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        cnt, result = {}, []
        for num in S:
            cnt[num] = cnt.get(num, 0) + 1
        c, S[:] = [0] * len(cnt), sorted(cnt.keys())
        while True:
            tmp = sum([[S[i]] * c[i] for i in xrange(len(c))], [])
            result.append(tmp)
            j = 0
            while j < len(S) and c[j] == cnt[S[j]]:
                c[j] = 0
                j += 1
            if j == len(S): break
            c[j] += 1
        return result
