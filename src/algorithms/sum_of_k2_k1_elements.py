# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
from heapq import *

class Solution:
  def findSumOfElements(self, nums, k1, k2):
    elementSum = 0
    # store k2 - 1 smallest numbers in a max-heap of same size
    # take out k2-k1 elements from the heap and sum them
    # return the sum
    max_heap = []
    for num in nums:
      if len(max_heap) < k2 - 1:
        heappush(max_heap, -num)
      else:
        if num < -max_heap[0]:
          heappop(max_heap)
          heappush(max_heap, -num)
    k2_k1 = k2 - k1 - 1
    while(k2_k1):
      elementSum += -heappop(max_heap)
      k2_k1 -= 1
    return elementSum
