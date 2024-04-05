#!/usr/bin/env python3
''' Basic cache Basic cache Basic cache Basic cache
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFO cache class
    '''

    def put(self, key, item):
        ''' Add an item in the cache
            and remove first if more than max items
        '''
        if key and item:
            self.cache_data[key] = item
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print("DISCARD: ", first)
                self.cache_data.pop(first)
                
    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            return self.cache_data[key]
