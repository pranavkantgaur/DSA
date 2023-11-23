class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:           
    def __init__(self, capacity):
        self.cap = capacity
        self.hMap = {}
        self.head = None
        self.tail = None

    def updateDLL(self, key): # dll: [2, 3, 4]
        # access node
        node = self.hMap[key][1]
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # if tail, do nothing        
        if node == self.tail:
            return
        # if head/mid put to back of DLL
        if node == self.head:
            self.head = node.next 
        # for head and mid nodes
        temp_next = node.next
        temp_prev = node.prev
        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        if temp_prev:
            temp_prev.next = temp_next
        if temp_next:
            temp_next.prev = temp_prev
        return 

    def evictLRU(self):
        # if capacity = 1
        lru_key = self.head.val
        if self.head == self.tail:
            del self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
        return lru_key # 1, dll:[2, 3]      

    def get(self, key):
        if key in self.hMap:
            self.updateDLL(key)
            return self.hMap[key][0]
        else:
            return -1
    def put(self, key, value):
        if key in self.hMap:
            self.updateDLL(key)
            self.hMap[key][0] = value
        else:
            # put in cache
            node = Node(key)
            if len(self.hMap) == self.cap:
                lru_key = self.evictLRU()
                del self.hMap[lru_key]
            self.hMap[key] = [value, node]
            self.updateDLL(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
