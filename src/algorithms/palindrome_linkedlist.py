#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def isPalindrome(self, head):
    # TODO: Write your code here
    '''
    1. Locate mid of ll
    2. Reverse the list till mid node
    3. Traverse and compare the remaining list with the reversed list
    4. If each node is comparable, return set True, else set False
    5. Reconstruct the original list
    6. Return status
    '''
    mid_node = self.getLLMid(head)
    head_reversed = self.getReversedLL(head, mid_node)
    while(sublist_1_node and sublist_2_node and sublist_1_node.val == sublist_2_node.val):
      sublist_1_node = sublist_1_node.next
      sublist_2_node = sublist_2_node.next
    is_palindrome = None
    if sublist_1_node == None and sublist_2_node == None:
      is_palindrome = True
    else:
      is_palindrome = False

    head = self.getReversedLL(head_reversed, head)


    return is_palindrome      
    
