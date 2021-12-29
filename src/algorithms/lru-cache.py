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
        the capacity of the cache should be intitialized.
        '''
        self.cap = capacity
        #print("Cap: ", self.cap)
        self.current_cache_size = 0
        self.hMap = {}
        self.cache_head = None
        self.cache_tail = None # points to the LRU item, for eviction

    def printCache(self):
        temp = self.cache_head
        print("Current cache: ")
        while(temp):
            print(temp.data)
            temp = temp.next
        print("REverse order:" )
        temp = self.cache_tail
        while(temp):
            print(temp.data)
            temp = temp.prev
            
    def get(self, key: int) -> int:
        '''
        returns the value of the key if it already exists in the cache otherwise returns -1.(O(1))
        '''
        
        if self.hMap and key in self.hMap.keys():            
            frame_node = self.hMap[key]
            if frame_node is not self.cache_head:
#                print("4: ? :" ,frame_node.prev.data)
                frame_node.prev.next = frame_node.next                
                if frame_node is self.cache_tail:
                    self.cache_tail = frame_node.prev
                else:
                    frame_node.next.prev = frame_node.prev
                    #print("YESY check")
                    #self.printCache()
                frame_node.prev = None
                frame_node.next = self.cache_head
                #print("Check")
                #self.printCache()
                self.cache_head.prev = frame_node
                self.cache_head = frame_node
            #self.printCache()
            return frame_node.data
        else:
            #self.printCache()
            return -1        

    def put(self, key: int, value: int) -> None:

        '''
        O(1)
        if the key is already present, update its value. If not present, add the key-value pair to the cache. 
        If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
        '''
        if not self.hMap:
            frame_node = Node(value) # also sets frame_node.next = None, frame_node.prev = None
            self.hMap[key] = frame_node            
            self.current_cache_size += 1
            self.cache_head = frame_node
            self.cache_tail = frame_node

        elif key in self.hMap.keys(): # key is in cache
            frame_node = self.hMap[key]
            frame_node.data = value
            #self.update_cache_head(frame_node, key) # only purpose is to bring frame_node to cache_head
            if frame_node is self.cache_head: 
    #            self.printCache()
                return 
            frame_node.prev.next = frame_node.next
            if frame_node is self.cache_tail:
                self.cache_tail = frame_node.prev
            frame_node.prev = None
            frame_node.next = self.cache_head
            self.cache_head.prev = frame_node
            self.cache_head = frame_node
        else: # key not in cache
            frame_node = Node(value) # also sets frame_node.next = None, frame_node.prev = None            
            if self.current_cache_size < self.cap:
                self.current_cache_size += 1
                self.hMap[key] = frame_node
                frame_node.next = self.cache_head
                self.cache_head.prev = frame_node
                self.cache_head = frame_node
            else:
                # evict LRU
                prev_tail_node = self.cache_tail
                if self.cache_tail is not self.cache_head:
                    self.cache_tail = self.cache_tail.prev
                    self.cache_tail.next = None
                # https://stackoverflow.com/a/13149770/985166
                evicted_node_key = list(self.hMap.keys())[list(self.hMap.values()).index(prev_tail_node)]
                self.hMap.pop(evicted_node_key) # remove reference to evicted node
                del prev_tail_node # remove evicted node from cache
                self.hMap[key] = frame_node
                frame_node.next = self.cache_head
                self.cache_head.prev = frame_node
                self.cache_head = frame_node
     #   self.printCache()                   

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
