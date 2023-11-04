# https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1

class Node:
  def __init__(self, data):
    self.val = data
    self.next = None
class MyQueue():
  self.head = None
  self.tail = None
  def push(node):
    # push to the end of linked list
    if self.head:
      self.tail.next = node
      self.tail = node
    else:
      self.head = node
      self.tail = node
    
  def pop():
    # pop from the head
    if self.head:
      temp = self.head
      self.head = self.head.next
      del temp
    else:
      return -1
