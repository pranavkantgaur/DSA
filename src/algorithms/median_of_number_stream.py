# Design a class to calculate the median of a number stream. The class should have the following two methods:

#    insertNum(int num): stores the number in the class
#    findMedian(): returns the median of all numbers inserted in the class

# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

from heapq import *

class Solution: 

  def __init__(self):
    self.min_heap = [] # store upper half
    self.max_heap = [] # store lower half

  def insertNum(self, num):
    if len(self.max_heap)==0: 
      heappush(self.max_heap, -num)
      return
    # if num > max_heap: 
    if num > -self.max_heap[0]:
    # check if len(min_heap) + 1 - len(max_heap) > 1: remove item from min_heap and push it to max_heap and push num to min_heap    
      if len(self.min_heap) > len(self.max_heap):
        element = heappop(self.min_heap)
        heappush(self.max_heap, -element)
        heappush(self.min_heap, num)
    # else, push the num to min_heap
      else:
        heappush(self.min_heap, num)
    # if num < max_heap:
    elif num < -self.max_heap[0]:
      #check if len(max_heap) + 1 - len(min_heap) > 1:  remove item from max_heap and push it to min_heap and push num to max_heap    
      if len(self.max_heap) > len(self.min_heap):
        element = -heappop(self.max_heap)
        heappush(self.min_heap, element)
        heappush(self.max_heap, -num)
      else:
        heappush(self.max_heap, -num)
    elif num  == -self.max_heap[0]:
      #push the num to the heap with smaller size, if the size of heaps is equal then it means the total numbers seen so far are even, 
      if len(self.max_heap) - len(self.min_heap) > 0: 
        heappush(self.min_heap, num)
      elif len(self.max_heap) - len(self.min_heap) < 0:           
        heappush(self.max_heap, -num)
      else:
        heappush(self.min_heap, num)  


  def findMedian(self):
    if len(self.max_heap) == 0: return None # no data in the stream.
    if (len(self.min_heap) + len(self.max_heap)) % 2: 
      if len(self.max_heap) > len(self.min_heap):
        return float(-self.max_heap[0])
      else:
        return float(self.min_heap[0])
    else: 
      return (-self.max_heap[0] + self.min_heap[0])/2
