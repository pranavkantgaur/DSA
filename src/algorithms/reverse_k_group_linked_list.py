# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

#  def print_list(self):
#    temp = self
#    while temp is not None:
#      print(temp.val, end=" ")
#      temp = temp.next
#    print()


#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

#  def print_list(self):
#    temp = self
#    while temp is not None:
#      print(temp.val, end=" ")
#      temp = temp.next
#    print()

class Solution:
  def reverse(self, head, k):
    '''
    1. store left sublist tail
    2. store to be reversed sublist head
    3. reverse sublist
    4. set left sublist.next = qth node
    5. set reversed_sublist_head.next = qth node.next
    6. set left sublist tail = reveresed sublist head
    7. reversed sublist head = reversed_sublist_head.next
    8. continue this untill next sublist size is less than k
    '''
    prev = None
    current = head
    while(True):              
      left_sublist_tail = prev
      sublist_head = current
      # reverse between sublist head and prev
      i = 0
      while(i < k and current):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        i += 1
      if left_sublist_tail:
        left_sublist_tail.next = prev
      else:
        head = prev
      sublist_head.next = current
      prev = sublist_head
      if not current:
        break
    return head               
        
