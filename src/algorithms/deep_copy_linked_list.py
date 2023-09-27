'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/

Deep copy a linked list with random pointers
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.


Clarify:
1. LL of length 1?
2. Can multiple nodes have same random_index?
3. Expected TC/SC:> O(n), O(1)
4. Self loops?

Test-cases:
1. [[1, 1], [4, 0]] -> deep copy # cycle case
2. [[1, 2], [4, 0], [7, 1]] -> deep copy # cycle case
3. [[1, 2], [4, 0], [10, -1], [11, 4], [1, 3]] # Isolated cycles


BF algorithm: TC:O(n) , SC: O(n)
1. Create new nodes by visiting the original list and initializing value and next pointers. Also, store <original_node, new_node> mapping in the hashmap.
2. Update random pointer: use hashmap
   1. For each node in original list, random list, new_node.random_index = hMap[original_node.random_index]
3. Return the head of new list   


# new ll is created but random ptrs are not initialized
prev_node = None
original_node = original_head
hMap = {}
while(original_node is not None):
  new_node = Node(original_node.val)  
  new_node.next = None
  if prev_node is not None:
  	prev_node.next = new_node 	
  else:
     new_ll_head = new_node	  	 	  	
  prev_node = new_node
  hMap[original_node] = new_node # can we index a dict with object address?
  original_node = original_node.next

# set random pointers for new ll
original_node = head
new_node = new_ll_head
while(original_node is not None):
  new_node.random = hMap[original_node.random]	
  original_node = original_node.next

return new_ll_head


Bottleneck:
0. Can it be done in O(1) space?
   * How to recall, if I have created the corresponsing new node already for the node pointed to by the random pointer in the original list's node?
1. Can set random_index in the same 1st pass?
   * Yes
   
   
# modified implementation with random_index setting in the first pass:
1. for each node in original list:
   1. create a new node and add the corresponding entry in node-node mappings   
   2. update the next poitner of previous node in new list and newly created node.
   3. update the random poimter of new node as: new_node.random = original_node.random ?? # random of original node may be pointing the a node not yet created in new list, 
      1. CREATE NEW NODE IF THE CORRESPONDING NODE POINTED TO BY RANDOM POINTER IS NOT THERE IN THE NEW LIST YET
      2. CONTINUE

'''
