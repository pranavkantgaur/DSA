#User function Template for python3


'''
SET x y : sets the value of the key x with value y
GET x : gets the key of x if present else returns -1.


Expected Time Complexity: O(1) for both get() and set().
Expected Auxiliary Space: O(1) for both get() and set(). 


Input:
cap = 2
Q = 2
Queries = SET 1 2 GET 1
Output: 2

Approach:
Cache design: 
 * Hashtable?: 
   * capacity: hashtable of size 'cap': maintaining a var representing cap of hashtable, and a counter to represent 
               curent size of cache
   * get(key): Looksup the key in hashtable, if found return value else -1, o(1), if found return value and update LRU key
   * set(key, value): 
     * Update the value in hashtable for a key if key is found, 
     * if key not present, check size of cache, if current_cache_size == capacity, invalidate LRU key, 
       value and add to the hashtable(update current cache size)
    * how to invalidate LRU key?: how to track LRU key in hashtable?
 * DoublyLinkedList Q with hashtable, H?
  * Frame are in Q which is of capacity 'cap', H contains pointer to each node in Q
  * capacity: keep 'cap' and 'current_size'# sets number of nodes in Q, 
  * get(key): O(1) ?
    * frame_node_in_cache = H[key]
    * if frame_node is not head, remove frame_node in cache from current position and put it at the head of queue
    * if frame_node not found in H[key], return -1
  * set(key, value): O(1)?
    * frame_node = H[key]
    * if frame_node:
      * frame_node.data = value
      * if frame_node is not head:
        * set frame_node as head
    * else:
      * if len(H) == 'cap':
        * # evict LRU key, val from Q and H
      * # create new node in Q with input (key, value)
      * # set new node as head of Q
      * # update H[ley] = new_node

'''


# design the class in the most optimal way
class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.data = value



class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        '''
        the capacity of the cache should be intitialized.
        '''
        self.cap = cap
        self.current_cache_size = 0
        #self.cache = None
        self.hMap = {}
        self.cache_head = None
        self.cache_tail = None
        
    def print_cache(self):
        temp = self.cache_head
        while(temp):
            print("value: ", temp.data)
            temp = temp.next
            
    def update_cache_head(self, frame_node, key):
        if not self.cache_head: # empty cache, update called
            self.cache_head = frame_node
            self.cache_tail = frame_node
        if frame_node is not self.cache_head: # if accessed node is not head
            if frame_node == self.cache_tail: # is it tail?
                self.cache_tail = frame_node.prev
                self.cache_tail.next = None
            else:
                if key in self.hMap.keys():
                    #print("FRAME: ", frame_node.next)
                    assert(frame_node.next.prev)
                    assert(frame_node.prev)
                    frame_node.next.prev = frame_node.prev
                else: # the updation method has been called with a newly created framenode
                    pass
            frame_node.next = self.cache_head
            frame_node.prev = None
            self.cache_head = frame_node
        else:
            return # do nothing as the LRU node is already at head
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        '''
        returns the value of the key if it already exists in the cache otherwise returns -1.(O(1))
        '''
        print("GET: {}".format(key))
        if key in self.hMap.keys():
            self.update_cache_head(self.hMap[key], key) # put this node to the head
            temp = self.cache_head
            print("After GET: ")
            self.print_cache()
            return self.hMap[key].data
        else:
            return -1

        
    #Function for storing key-value pair.   
    def set(self, key, value):
        #code here
        '''
        O(1)
        if the key is already present, update its value. If not present, add the key-value pair to the cache. 
        If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
        '''
        print("SET: {}, {}".format(key, value))
        if not self.hMap:
            frame_node = Node(value) # also sets frame_node.next = None, frame_node.prev = None
            self.hMap[key] = frame_node            
            self.current_cache_size += 1
        elif key in self.hMap.keys(): # key is in cache
            frame_node = self.hMap[key]
            frame_node.data = value
            self.update_cache_head(frame_node, key)
        else: # key not in cache
            frame_node = Node(value) # also sets frame_node.next = None, frame_node.prev = None
            self.hMap[key] = frame_node
            if self.current_cache_size < self.cap:
                self.current_cache_size += 1
            else:
                # evict LRU
                prev_tail_node = self.cache_tail
                self.cache_tail = self.cache_tail.prev
                self.cache_tail.next = None
                # https://stackoverflow.com/a/13149770/985166
                evicted_node_key = list(self.hMap.keys())[list(self.hMap.values()).index(prev_tail_node)]
                self.hMap.pop(evicted_node_key) # remove reference to evicted node
                del prev_tail_node # remove evicted node from cache
        self.update_cache_head(frame_node, key)    
        print("After SET: ")
        self.print_cache()
            
                    
                                
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends
