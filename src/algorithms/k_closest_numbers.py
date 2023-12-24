# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.
from heapq import heappush, heappop
class Solution:
  def binary_search(self, arr, X):
    low = 0
    high = len(arr) - 1
    while(low < high):
      mid = low + (high - low) // 2
      if arr[mid] == X:
        return mid
      elif arr[mid] < X:
        low = mid + 1
      else:
        high = mid - 1
    return left
    
  def findClosestElements(self, arr, K, X):
    if len(arr) < K: return []
    result = []
    '''
    1. push elements of arr based on distance of number wrt. x in a heap of size k
    2. once the size is == k, then ignore new element if the its distance is > that of max heap top else remove
    max heap top and push current number
    '''
    index = self.binary_search(arr, X)
    low = max(0, index - K)
    high = min(len(arr) - 1, index + K)
    max_heap = []
    for num in arr[low: high + 1]:
      if len(max_heap) < K:
        item = (-abs(num - X), num) # push into max heap based on distance from X
        heappush(max_heap, item)
      else:
        if -max_heap[0][0] > abs(num - X):
          heappop(max_heap)
          item = (-abs(num - X), num)
          heappush(max_heap, item)
    while(len(max_heap)):
      result.append(heappop(max_heap)[1])
    return result[::-1]
