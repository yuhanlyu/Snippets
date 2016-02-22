class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        if not s or len(s) > 12: return []
        DP1 = [[] for _ in xrange(len(s))]
        for i in xrange(len(s)):
            DP1[i] = [s[i:i + 1]]
            if s[i] != '0' and i + 2 <= len(s): DP1[i].append(s[i:i + 2])
            if s[i] != '0' and i + 3 <= len(s) \
            and int(s[i:i + 3]) <= 255: DP1[i].append(s[i:i + 3])
        DP2 = [[[p, q] for p in DP1[i] if i + len(p) < len(s)
                       for q in DP1[i + len(p)]] for i in xrange(len(s))]
        return ['.'.join(p + q) for p in DP2[0] if len(''.join(p)) < len(s)
                                for q in DP2[len(''.join(p))]
                                if len(''.join(p + q)) == len(s)]
