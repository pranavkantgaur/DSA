# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.
from heapq import *

class Solution:
  def findMaximumDistinctElements(self, nums, k):
    distinctElementsCount = 0
    hmap = {}
    min_heap = []
    for num in nums:
      if num in hmap:
        hmap[num] += 1
      else:
        hmap[num] = 1
    for key in hmap: # push non-distinct elements to priority-queue
      if hmap[key] > 1:
        item = (hmap[key], key)
        heappush(min_heap, item)
    while(k > 0 and len(min_heap)):
      count, key = heappop(min_heap) # reduce count of the least frquent number
      hmap[key] -= 1
      count = hmap[key]
      if count > 1:
        heappush(min_heap, (count, key)) # reinsert the item into heap
      k -= 1
    for key in hmap:
      if hmap[key] == 1:
        distinctElementsCount += 1  
    distinctElementsCount -= k
    return distinctElementsCount
