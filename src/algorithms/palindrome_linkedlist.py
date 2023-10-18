# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TC: O(n), SC: O(1)
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def reverseLL(self, head):
    prev = None
    while(head):
      t = head.next
      head.next = prev
      prev = head
      head = t
    return prev

  def isPalindrome(self, head):
    slow = head
    fast = head
    while(fast and fast.next): # get mid node
      slow = slow.next
      fast = fast.next.next
    reversed_head = self.reverseLL(slow)
    while(reversed_head and head): # palindrome check
      if reversed_head.val != head.val:
        break
      reversed_head = reversed_head.next
      head = head.next

    #reversed_head = self.reverseLL(reversed_head)

    if not reversed_head or not head:
      return True
    else:
      return False              

        
