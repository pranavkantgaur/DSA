# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

class Solution:
  def searchQuadruplets(self, arr, target):
    quadruplets = []
    '''
    1. sort array
    2.  for each num1:
         1. iterate on remaning nums, num2:
             1. Set target1 = target - num1 - num2
                1. rUN 2 ptrs to look for a tuple with sum =  target1                
    '''
    arr.sort()
    for id1 in range(len(arr) - 3):
      if id1 > 0 and arr[id1] == arr[id1 - 1]:
        continue
      for id2 in range(id1 + 1, len(arr[id1+1:]) - 2):
        if id2 > id1 + 1 and arr[id2] == arr[id2 - 1]:
          continue
        target_1 = target - arr[id1] - arr[id2]        
        left = id1 + id2 + 1
        right = len(arr) - 1
        while(left < right):
          current_sum = arr[left] + arr[right]
          if current_sum < target_1:
            left += 1
          elif current_sum > target_1:
            right -= 1
          else:
            quadruplets.append([arr[id1], arr[id2], arr[left], arr[right]]) 
            left += 1
            right -= 1
            while(left < right and arr[left] == arr[left - 1]):
              left += 1
            while(left < right and arr[right] == arr[right + 1]):
              right -= 1                                         
    return quadruplets
