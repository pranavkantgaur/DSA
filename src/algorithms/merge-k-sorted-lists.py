# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Approach - 1: Merge 2 lists at a time for k - 1 times

'''
class Solution:
    def merge2Lists(self, merged_list, next_list):
        result_list = []
        node1 = merged_list[0]
        node2 = next_list[0]
        while node1 is not None:            
            if node1.val >= node2.val:
                result_list.append(node2)
                if result_list:
                    result_list[-1].next = node2
            if result_list:
                result_list[-1].next = node1
            result_list.append(node1)   
            result_list[-1].next = None
            node1 = node1.next
        return result_list          
            
                
                
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = list[0]
        for next_list in range(lists[1:]):
            merged_list = self.merge2Lists(merged_list, next_list)
        return merged_list    
        
