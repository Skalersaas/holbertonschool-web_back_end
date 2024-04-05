''' Basic cache Basic cache Basic cache Basic cache
'''

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    ''' MRU cache class
    '''
    list = {}
    def put(self, key, item):
        ''' Add an item in the cache
            and remove first if more than max items
        '''
        if key and item:
            self.cache_data[key] = item
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print("DISCARD:", first)
                self.cache_data.pop(first)
            list[key] = 0

    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = value
            list[key] += 1
            return value
my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()