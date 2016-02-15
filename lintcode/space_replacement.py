class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        num = 0
        for i in xrange(length):
            if string[i] == " ":
                num += 1
        tail = length + num * 2 - 1
        for i in xrange(length - 1, -1, -1):
            if string[i] != " ":
                string[tail] = string[i]
                tail -= 1
            else:
                string[tail] = "0"
                string[tail - 1] = "2"
                string[tail - 2] = "%"
                tail -= 3
        return length + num * 2
