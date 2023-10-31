# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/merge-k-sorted-lists
# Other solutions:
'''
https://leetcode.com/problems/merge-k-sorted-lists/discuss/1810642/C%2B%2B-oror-Priority-Queue-oror-23.-Merge-k-Sorted-Lists
1. Creates a priority queue, inserting all input linked lists, sorted based on node values: HOW??
   1.1. Each node in the queue is <value, node-pointer>
   1.2. How q.push({list->val,list}); works for priority_queue<pair<int,ListNode*>,vector<pair<int,ListNode*>>,greater<pair<int,ListNode*>>>q; ?
2. Pops out elements from priority queue one at a time, building the final linked list in the process.
TC: O(nlogk): HOW??

Similar to our solution:
* https://leetcode.com/problems/merge-k-sorted-lists/discuss/10531/Sharing-my-straightforward-C%2B%2B-solution-without-data-structure-other-than-vector

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        1. list of running pointers across k lists
        2, at each iteration get the min value node from heap, remove it from the heap and add next node from same list into the heap
        3. connect the next of prev node to this node
        4. set prev node = current node
        5. continue till heap is empty
        '''
        min_heap = []
        for ll in lists:
            item = (ll.val, ll)
            heapq.heappush(min_heap, item)
        prev = None
        while(len(min_heap)):
            _, node = heapq.heappop(min_heap)
            if prev:
                prev.next = node
                prev = node
            else:
                prev = node
                head = node
            
            if node.next:
                item = (node.val, node.next)
                heapq.heappush(min_heap, item)
        return head
