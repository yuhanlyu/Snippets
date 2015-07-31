# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.
# get(key) - Get the value (will always be positive) of the key if the key 
# exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently 
# used item before inserting a new item.
# Time Complexity: O(1) for each operation
# Space Complexity: O(n)

from collections import OrderedDict

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    # @return an integer
    def get(self, key):
        if not key in self.cache: return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(False)
        self.cache[key] = value
                                                        
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.set("a", 1)
    lru.set("b", 2)
    lru.set("c", 3)
    print lru.get("a")
