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
    return low
    
  def findClosestElements(self, arr, K, X):
    if len(arr) < K: return []
    result = []
    '''
    1. push elements of arr based on distance of number wrt. x in a heap of size k
    2. once the size is == k, then ignore new element if the its distance is > that of max heap top else remove
    max heap top and push current number
    '''
    index = self.binary_search(arr, X)
    left = index
    right = index
    print('num: ', arr[index])
    while(left >= 0 and right <= len(arr) - 1 and len(result) < K):
      left_diff = abs(arr[left] - X)
      right_diff = abs(arr[right] - X)
      if left_diff < right_diff:
        result.append(arr[left])
        left -= 1  
      elif left_diff > right_diff:
        result.append(arr[right])
        right += 1
      else:
        if left == right: 
          result.append(arr[left])
          left -= 1
          right += 1
          continue
        result.append(arr[left])
        left -= 1
        if left >= 0 and right - left < K:
          result.append(arr[right])
          right += 1
    print('res: ', len(result), right, left)
    # TODO: fix for termination of loop before k elements
    while(len(result) < K):
      if left >= 0:
        result.append(arr[left])
        left -= 1
      if right <= len(arr) - 1:
        result.append(arr[right])
        right += 1
    result.sort()
    return result
