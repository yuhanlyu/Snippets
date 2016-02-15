class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        result = ['1']
        for _ in xrange(n - 1):
            tmp, count, index = [], 1, 0
            while index < len(result):
                if index == len(result) - 1 or result[index+1] != result[index]:
                    tmp.extend(str(count))
                    tmp.append(result[index])
                    count = 1
                else:
                    count += 1
                index += 1
            result = tmp
        return ''.join(result)
