# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next



class Solution:
  def reverse(self, head):
    prev = None
    while(head):
      t = head.next
      head.next = prev
      prev = head
      head = t
    return prev

  def reorder(self, head):
    '''
    1. get mid node
    2. reverse ll from mid node onwards
    3. for each node in reverse ll, and first ll head:
       t = firstll_head.next
       firstll_head.next = reversell_head
       q = reverse_ll_head.next
       reverse_ll_head.next = t
       firstll_head = t
       reverse_ll_head = q
    4. return head       
    '''
    slow = head
    fast = head
    while(fast and fast.next):
      slow = slow.next
      fast = fast.next.next
    rev_head = self.reverse(slow)      
    head_copy = head
    while(head_copy and rev_head):
      t = head_copy.next
      q = rev_head.next
      head_copy.next = rev_head
      rev_head.next = t
      head_copy = t
      rev_head = q
      if t == q:
        break
    #head = head_copy
    return head
