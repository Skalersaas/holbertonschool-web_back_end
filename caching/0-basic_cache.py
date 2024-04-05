#!/usr/bin/env python3
''' Basic cache
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Basic cache class
    '''


    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key and item:
            self.cache_data[key] = item


    def get(self, key):
        ''' Get an item by key
        '''
        if key and key in self.cache_data:
            return self.cache_data[key]
