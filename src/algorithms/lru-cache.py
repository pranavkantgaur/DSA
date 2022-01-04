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
        self.cache_head = Node(0) # dummy value
        self.cache_tail = Node(0)
        self.cache_head.next = self.cache_tail
        self.cache_tail.prev = self.cache_head
    
    def _add_node(self, frame_node):
        frame_node.next = self.cache_head.next
        frame_node.prev = self.cache_head        
        self.cache_head.next.prev = frame_node
        self.cache_head.next = frame_node
    
    def _remove_node(self, frame_node):
        frame_node.prev.next = frame_node.next
        frame_node.next.prev = frame_node.prev        
        del frame_node
            
    def get(self, key: int) -> int:
        if key in self.hMap.keys():
            frame_node = self.hMap[key]
            new_node = Node(frame_node.data)
            self._remove_node(frame_node)
            self._add_node(new_node)
            self.hMap[key] = new_node
            return new_node.data
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.hMap.keys():
            frame_node = self.hMap[key]
            self._remove_node(frame_node)
        else:
            if self.current_cache_size < self.cap:                
                self.current_cache_size += 1
            else:
                del self.hMap[list(self.hMap.keys())[list(self.hMap.values()).index(self.cache_tail.prev)]]
                self._remove_node(self.cache_tail.prev)
                
        new_node = Node(value)
        self._add_node(new_node)       
        self.hMap[key] = new_node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
