# Design a class to efficiently find the Kth largest element in a stream of numbers.

#The class should have the following two things:

#The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
#The class should expose a function add(int num) which will store the given number and return the Kth largest number.
  
from heapq import *

class Solution:
  def __init__(self, nums, k):
    self.min_heap = []
    self.k = k
    for num in nums:
      self.add(num)
    return

  def add(self, num):
    if len(self.min_heap) < self.k:
      heappush(self.min_heap, num)
    else:
      if num > self.min_heap[0]:
        heappop(self.min_heap)
        heappush(self.min_heap, num)
    return self.min_heap[0]
