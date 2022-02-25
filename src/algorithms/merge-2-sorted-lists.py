# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
1. Iterative
   1. Start with first node in list1:
      1.1. check if it is smaller than first node in list2, 
      1.2. if not add node2 in new list till the value of node in list2 is less than or equal to node 1
      1.3. add node1 to the result list
   2. if there are nodes in list2 add them to result list   
   
2. Recursive: https://leetcode.com/problems/merge-two-sorted-lists/discuss/9715/Java-1-ms-4-lines-codes-using-recursion
   if list1 is None: return list2
   if list2 is None: return list1
   if l1.val < l2.val:
      l1.next = merge2Lists(l1.next, l2)
   else:
      l2.next = merge2Lists(l1, l2.next)
      
3. Iterative, in-place:
   * Given 2 sorted lists, merge them in-place: Inplace-merging means creating merged linked-list without using additional space (i.e., SC: O(1)).
   * Maintain 3 head pointers, 1 each for part of list1, list2 remaining to be processed and 1 for result list
   * start with list1: check if first item of list1 is smaller than that of list2, if so, make list1's first node as head of result list: resultHead = list1[0] 
     and advance list1head (thereby shrinking list1 and expanding resultList)
     * if node in list2 is smaller than node in list1 then resultHead = list2[0]
       * for all subsequent nodes in list2 with value less than that of the node pointed to by head of list1: continue traversing list2 and advancing list2head
         (advancing list2 head has the effect of list2 getting shrunked and resultlist expanding)    
   * At the end of loop, when either list1 or list2 is empty, return head   
'''
      
'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''



class Solution:
    def mergeTwoListsInPlace(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
                if resultList:
                    resultList[-1].next = node1
                resultList.append(node1)    
                resultList[-1].next = None
                node1 = node1.next
            #2. If list2 is not None: # at this point list1 is exhausted.
            #   Append list2 to the result            
            while node2 is not None:
                resultList[-1].next = node2
                resultList.append(node2)                
                node2 = node2.next         
            
            #3. return head of the result list               
            return resultList[0]    
