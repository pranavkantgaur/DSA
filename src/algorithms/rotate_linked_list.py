'''
# https://leetcode.com/problems/rotate-list/description/
Rotate a linked list:
Given the head of a linked list, rotate the list to the right by k places.

Clarify:
1. Output is same linked list?
2. How to rotate linked list of size 1?
3. Expected TC/SC?
4. 

Test-cases:
1. 36982, K = 3, => 98236?
2. 36982, k =10 => 36982, no. of right shifts -> k mod n 
3. 36982, k  = 12, 12 mod 5 = 2 -> 82369

BF approach: TC-> O(max(n, k)), SC: O(n)
1. Traverse the list, copy the node-values in an array
2. Rotate the array
3. Visit the linked list again and overwrite the node-values with corresponding values in the array.

Another approach with TC = O(min(n, k)), SC = O(1)?
1. Go to the just preceding node to the k mod n th node in linked list, k_1_th_node
2. tail.next = head, k_1_th.next = null, head = kth_node

What are the cases where this fails?
* TODO


Observations:
1. Nodes which are in the mid need not to have their linked changed, only the kth last node and the tail node's next pointers need to change.
2. 


'''
