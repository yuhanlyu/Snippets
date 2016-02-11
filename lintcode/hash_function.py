class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        result = 0
        for x in list(key):
            result = (result * 33 + ord(x)) % HASH_SIZE
        return result
