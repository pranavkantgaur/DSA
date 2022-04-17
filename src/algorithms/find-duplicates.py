# https://www.pramp.com/challenge/15oxrQx6LjtQj9JK9XlA
'''
input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7]

1. M = N
2. M >> N

BF:
1. For each number in arr1:
   1.1 Check if it exisits in arr2:
       1.1.1. if true: add to result array
   1.2. return result
TC: O(M*N)
SC: O(1)

Binary search:
TC: O(M*logN)
SC: O(1)

Hash:
TC: O(M)
SC: O(N)
'''
#from collections import Counter

def b_search(target, arr):
    first = 0
    last = len(arr) - 1
    while first <= last: 
      mid = first + (last - first) // 2
      if arr[mid] == target:
        return True
      elif arr[mid] > target:
          last = mid - 1
          #b_search(target, arr[:mid-1])          
      else:
          #b_search(target, arr[:mid+1])
          first = mid + 1
    return False

  
  
  
def find_duplicates(arr1, arr2):
  # hash approach:
  duplicate_pass_nums = []
  #arr2_hmap = Counter(arr2)
  for pass_num in arr1:
      #if pass_num in arr2_hmap:
      if b_search(pass_num, arr2):
        duplicate_pass_nums.append(pass_num)
      #else:
      #  continue
      
  return duplicate_pass_nums    
  #arr2_hmap[0]
  
  
  
  #pass # your code goes here
