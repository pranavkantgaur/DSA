# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
class Solution:
  def findMax(self, arr):
    left = 0
    right = len(arr) - 1
    while(left <= right):
      mid = left + (right - left) // 2
      if mid == 0:
        if arr[mid] > arr[mid + 1]:
          return arr[mid]
        else:
          left = mid + 1
      elif mid == len(arr) - 1:  
        if arr[mid] > arr[mid - 1]:
          return arr[mid]
        else:
          right = mid - 1
      elif arr[mid - 1] < arr[mid] > arr[mid + 1]:
        return arr[mid]
      elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
        right = mid - 1
      elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
        left = mid + 1  
    return -1
