'''
# https://leetcode.com/problems/reverse-linked-list/description/

Clarify:
1. TC, SC-> O(n), O(1)
2. Always solvable: Yes


Test-cases:
1. [] [] -> []
2. [] [1] -> [1]
3. [1, 3], [1, 9] -> [1,1, 9]
4. [1,1], [1,1] -> [1,1,1,1]
5. [5, 8], [2, 9] -> [2, 5, 8, 9]


Naive algprotm
1. Maintain a hmap, visit each lists node and identify which node will come at each index
2. hmap's key is the index number of the resulting merged list
3. for each key, we store the previous(to the target) node's reference
4. In the second pass,
   1. For each key visited in the ascending order of index,
      1. Get the prev. node address, use that to get address of the target node
      2. Also, get the address of target node.next
      3. set prev. node.next = target node.next
      4. merged_list_current_node.next = target_node
      5. target_node.next = None
      6. merged_list_current_node = target_node
'''
