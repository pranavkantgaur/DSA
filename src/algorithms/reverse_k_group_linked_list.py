# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
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

class Solution:
  def reverse(self, head, k):
    # TODO: Write your code here
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
    left_sublist_tail = prev
    sublist_head = current
    while(True):
      # create window of size k if possible
      # reverse the list within this window
      # update pointers: left sublist next, original head of reversed sublist next
      # set pointers: left sublist, head of sublist to be reversed
      # go back to step-1
      # if not possible, come-out of this loop              
      i = 0
      while(current and i < k):
        prev = current
        current = current.next
        i += 1
      # prev is the kth node
      if i < k: # remaining sublist is smaller than k
        break
      if left_sublist_tail is None:
        head = prev
      # reverse between sublist head and prev
      i = 0
      prev  = left_sublist_tail
      current = sublist_head
      while(i < k):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        i += 1
      left_sublist_tail.next = prev
      sublist_head.next = current  
      left_sublist_tail = prev
      sublist_head = current      

    return head
               
        
