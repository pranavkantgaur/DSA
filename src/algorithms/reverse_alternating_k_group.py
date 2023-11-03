# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

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
    1. set sublist_id = 0, for even subklist id, reverse the sublist 
    2. for odd sublist id, skip the sublist by traversing to the end of it
    3. set left sublist tail and sublist head for connecting subslists post reversal
    4. if current pointer get none, break out of this loop and return the head.
    '''
    sublist_id = 0
    prev = None
    current = head
    while(True):
      if sublist_id % 2 == 0:
        # reverse sublist
        left_sublist_tail = prev
        sublist_head = current
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
      else:
        # skip list
        i = 0
        while(i < k and current):
          prev = current
          current = current.next
          i += 1
      sublist_id += 1
      if not current:
        break
    return head
