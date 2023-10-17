# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  
  def getLinkedListCycleLength(head):
    # reach inside cycle
    fast = head
    slow = head
    while(fast != slow):
      slow = slow.next
      fast = fast.next.next
    k = 0
    while(fast != slow):
      slow = slow.next
      fast = fast.next.next          
      k += 1
    # increment the counter untill fast = slow again
    return k
  def getKthNodeFromPointer(node, k):
    while(count < k):
      node = node.next
      count += 1
    return node      

  def findCycleStart(self, head):
    #TODO Write your code here
    k = self.getLinkedListCycleLength(head)
    slow = head
    counter = 0
    while(counter < k):
      fast = fast.next
    while(fast != slow):
      slow = slow.next
      fast = getKthNodeFromPointer(slow, k)
    return slow
