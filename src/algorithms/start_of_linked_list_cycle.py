# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  

#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def findCycleStart(self, head):
    '''
    1. Reach inside cycle : O(n), O(1)
    2. Compute length of the cycle, k : O(k), O(1)
    3. Set first and last pointer with a gap k, O(k), O(1)
    4. Iterate first and last pointer until last.next != first : O(n), O(1)
    5. Return first 
    '''
    slow = head
    fast = head
    while(fast and fast.next): # get inside cycle
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        break
    first = slow
    last = slow.next
    k = 0
    while(last != first): #  get cycle length
      k += 1
      last = last.next     
    first = head
    last = head
    while(k > 0):    # set sliding window
      last = last.next
      k -= 1
    # sliding window    
    while(first != last.next): # slide the window
      first = first.next
      last = last.next
    return first            

