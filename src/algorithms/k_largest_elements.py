# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
from heapq import heappush, heappop
class Solution :
  def findKLargestNumbers(self, nums, k):
    if len(nums) < k: return []
    min_heap = []
    for num in nums:
      if len(min_heap) < k:
          heappush(min_heap, num)
      else:
          if num > min_heap[0]:
              heappop(min_heap)
              heappush(min_heap, num)
    result = []
    while(len(min_heap)):
      result.append(heappop(min_heap))
    return result
