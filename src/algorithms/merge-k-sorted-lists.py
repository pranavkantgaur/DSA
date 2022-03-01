# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1head = list1
        list2head = list2
        resulthead = None
        resulttail = None
        while list1head and list2head:
            if list1head.val < list2head.val:
                if not resulthead:
                    resulthead = list1head         
                    resulttail = list1head
                    
                else:
                    resulttail.next = list1head
                    resulttail = list1head
                list1head = list1head.next
            else:
                if not resulthead:
                    resulthead = list2head         
                    resulttail = list2head
                else:
                    resulttail.next = list2head
                    resulttail = list2head
                list2head = list2head.next            
        if list1head:
            if resulttail:
                resulttail.next = list1head
            else:
                resulthead = list1head
        if list2head:
            if resulttail:
                resulttail.next = list2head
            else:
                resulthead = list2head
        return resulthead

    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = lists[0]
        for next_list in lists[1:]:
            merged_list = self.mergeTwoLists(merged_list, next_list)
        return merged_list  
        
