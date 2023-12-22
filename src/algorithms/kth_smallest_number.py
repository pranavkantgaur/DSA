# Given an unsorted array of numbers, find Kth smallest number in it.

# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

from heapq import *

class Solution:
  def findKthSmallestNumber(self, nums, k):
    '''
    1. max heap of size k
    2. insert  jumbers till size k is reached
    3. if num >= max_heap[0], then ignore, else, remove max_heap number and insert num
    4. return numbers in the heap at the end of traversing all numbers in nums.
    '''
    if len(nums) < k: return []
    max_heap = []
    for num in nums:
      if len(max_heap) < k:
        heappush(max_heap, -num)
      else:
        if num < -max_heap[0]:
          heappop(max_heap)
          heappush(max_heap, -num)
    return -max_heap[0]
