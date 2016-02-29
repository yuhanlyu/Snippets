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
