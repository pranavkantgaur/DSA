# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
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
  def reverse(self, head, p, q):
    # locate p - 1th node, mark it as left_sublist_tail
    # reverse sublist from pth to qth node
    # update p-1th nodes next pointer as = qth node
    # update pth nodes next pointer as qth nodes original next
    # return head  
    i = 0
    prev = None
    current = head
    while(i < p - 1):
      prev = current
      current = current.next
      i += 1
    # prev is pointing to the p-1th node
    left_sublist_tail = prev
    start_of_sublist = current
    i = 0
    while(i < q - p + 1):
      temp = current.next
      current.next = prev
      prev = current
      current = temp
      i += 1      
    # prev points to the qth node
    if left_sublist_tail:
      left_sublist_tail.next = prev
    else:
      head = prev
    start_of_sublist.next = current
    
    return head
