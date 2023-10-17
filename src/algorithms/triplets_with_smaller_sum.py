# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
class Solution:
  def searchTriplets(self, arr, target):
    count = 0
    arr.sort()
    for id in range(len(arr) - 2):
      left = id + 1
      right = len(arr) - 1
      while(left < right):
        current_sum = arr[id] + arr[left] + arr[right]
        if current_sum < target:
          count += right - left
          left += 1         
        else:
          right -= 1    

    return count
