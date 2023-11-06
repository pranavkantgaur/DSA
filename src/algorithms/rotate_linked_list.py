# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
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
  def rotate(self, head, rotations):
    '''
    1. reach the kth last node in ll
    2. set it as the new head of ll
    3. connect end node of ll to the previous head node
    4. return head
    '''
    prev_head = head
    left = head
    right = head
    i = 0
    while(i < rotations - 1):
      right = right.next
      i += 1   
    left_sublist_tail = None       
    while(right.next):
      left_sublist_tail = left
      left = left.next
      right = right.next    
    right.next = head
    if left_sublist_tail:
      left_sublist_tail.next = None
    head = left

    return head
