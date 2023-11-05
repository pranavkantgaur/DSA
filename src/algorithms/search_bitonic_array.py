# Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
# Write a function to return the index of the ‘key’. If the 'key' appears more than once, return the smaller index. If the ‘key’ is not present, return -1.
class Solution:
  def findMaxElement(self, left, right, arr):
    while(left < right):
      mid = left + (right - left) // 2
      if arr[mid] > arr[mid + 1]:
        right = mid
      else:
        left = mid + 1
    return left

  def bsearch(self, left, right, key, arr):
    while(left <= right):
      mid = left + (right - left) // 2
      if arr[mid] > key:
        right = mid - 1
      elif arr[mid] < key:
        left = mid + 1
      else:
        return mid
    return -1

  def search(self, arr, key):
    '''
    1. get index of max element in bitonic array, max_id, if arr[max_id] == key, return
    2. do binary search in 0-max_id, if key found, return 
    3. do binary search in max_id + 1 to n-1, if key found return
    '''
    # get max element in bitonic array
    max_id = self.findMaxElement(0, len(arr) - 1, arr)
    if arr[max_id] == key:
      return max_id
    # search in left subarray
    num_id = self.bsearch(0, max_id - 1, key, arr)
    # search in right subarray
    if num_id == -1:
      num_id = self.bsearch(max_id + 1, len(arr) - 1, key, arr)
    else:
      return num_id  
    return num_id
