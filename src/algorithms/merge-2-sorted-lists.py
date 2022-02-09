# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        elif list2 is None and list1 is not None:
            return list1
        elif list1 is None and list2 is None:
            return None
        else:            
            #0. Initialize result list
            resultList = []
            #1. For each node in list1:
            #   Append all nodes from list2 which are smaller or equal than this node to the result
            #   Append node to result
            #for node1 in list1:
            node1 = list1[0]
            node2 = list2[0]
            while node1 is not None:
                #node2 = list2[0]
                while node2.val <= node1.val:
                    if resultList:
                        resultList[-1].next = node2                        
                    resultList.append(node2)                                                                                  
                    node2 = node2.next
                resultList[-1].next = node1
                resultList.append(node1)    
                resultList[-1].next = None
                node1 = node1.next
            #2. If list2 is not None: # at this point list1 is exhausted.
            #   Append list2 to the result
            if list2 is not None:
                resultList.append(node2)                
                node2 = node2.next         
            
            #3. return head of the result list               
            return resultList[0]
            
