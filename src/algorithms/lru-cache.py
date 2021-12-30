'''
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

The functions get and put must each run in O(1) average time complexity.
Approch-1
0. function evictLRU():
   # identidy the index of LRU key:value pair  # how to make this O(1) with hashmap alone?
   # remove from cache , if hashmap: O(1)
1. What ds to use for O(1) get and O(1) put? 
   1.1. O(1) get or lookup -> hashtable = {key: value}-> if key in hmap return hMap[key] else, return -1 -> O(1)
        1.1.1 O(1) for put(key, value): 
              if key in hMap.keys() -> hMap[key] = value
              else:
                  if len(hMap) + 1 > capacity:
                     evictLRU(hMap) # TODO, how to make it O(1)
                  hMap[key] = value   
   
    
'''
class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.data = value
        
class LRUCache:

    def __init__(self, capacity: int):
        '''
        the capacity of the cache is set.
        the actual cache(represented as a doubly-linked-list) 
        will be created/updated on demand and will be limited by 
        the value in `cap` attribute of the LRUCache class.
        '''
        self.cap = capacity
        self.currentCacheSize = 0
        self.cacheNodePointers = {}
        self.cache_head = None 
        self.cache_tail = None # points to the LRU item, for eviction(if required).

    def printCacheContent(self):
        temp = self.cache_head
        print("Cache(forward): ")
        while(temp):
            print(temp.data)
            temp = temp.next
        print("Reverse order:" )
        temp = self.cache_tail
        while(temp):
            print(temp.data)
            temp = temp.prev
    
    def lruFy(self, frame_node, is_new_node):        
        '''
        this method restores the LRU ordering property of cache
        if input node is new and cache is empty:
          it adds input node at the top and updates tail and head of cache
        if input node is new and cache is not empty
           if the cache capacity is not reached:
             it adds input node at the top and ipdates cache head only
           if cache capacity is reached:
              it removes the tail node from cache and adds input node to the cache-head
              also, since the tail node is removed from the cache(and also from node 
              pointer dicitonary), it updates the tail pointer too.
        if input node is not new:
           if input node is at head already:
              does nothing and returns
           if input node is in the middle withing the cache:
              it takes out the input node from the cache(doubly-linked-list)
              and puts the node at the top, updating cache head pointer
           if input node is at the end(tail):
              it takes the node out from the cache and puts it at the head
              updates the head pointer and tail pointer
        '''
        pass

    def get(self, key: int) -> int:        
        '''
        checks if the key exisits in the pointer dict. it returns the data in the node
        also updates the cache as the node corresponding to input key is now the most recently 
        accessed node, it may update tail pointer too, in case the accessed node was at the tail
        of the cache.
        '''
        if self.hMap and key in self.hMap.keys():            
            frame_node = self.hMap[key]
            if frame_node is not self.cache_head: # LRU is updated.
                self.lruFy(frame_node, is_new_node = False)
            return frame_node.data
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if not self.hMap:
            frame_node = Node(value) # also sets frame_node.next = None, frame_node.prev = None
            self.lruFy(frame_node, is_new_node = True)
        elif key in self.hMap.keys(): # key is in cache
            frame_node = self.hMap[key]
            frame_node.data = value
            if frame_node is self.cache_head: # no LRU updation required.
                return 
            else:
                self.updatelruFy(frame_node, is_new_node = False)
        else: # key not in cache

                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
