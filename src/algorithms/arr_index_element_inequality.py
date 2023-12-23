def index_equals_value_search(arr):
  left = 0
  right = len(arr) - 1
  result = -1
  while(left <= right):
    mid = left + (right - left) // 2
    if arr[mid] - mid == 0:
      result = mid
      right = mid - 1
    elif arr[mid] - mid < 0:
      left = mid + 1
    else:
      right = mid - 1
  return result
  
  # your code goes here
  '''
  if arr[mid] < mid: 
     0 2 5
     
     mid = 1
     2 > 1
     
  arr[i] - i < 0 = 0 > 0
  
                arr[i] == i
            j < i
            arr[j] < arr[i] 
            
            arr[j] - j <= arr[i] - i
            
                   1  2   4  5
            0   1. 2 3. 4 5 6 7 8
                          0
            
            
            
            
  arr[i] - i == 0: left
  arr[i] - i < 0:
  '''
