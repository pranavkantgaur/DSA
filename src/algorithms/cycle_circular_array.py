# https://leetcode.com/problems/circular-array-loop/description/
'''
1 . for each starting position, set slow and fast pointer
2. continue to advance slow and fast pointer untill slow == fast or the next movement is in the opposite direction
3. if fast == slow check if the length of cycle is greater than 1 return true
4. if fast != slow and we came out of while loop, return false
TC: O(n^2), SC: O(1)
'''

'''
1 . for each starting position, set slow and fast pointer
2. continue to advance slow and fast pointer untill slow == fast or the next movement is in the opposite direction
3. if fast == slow check if the length of cycle is greater than 1 return true
4. if fast != slow and we came out of while loop, return false
TC: O(n^2), SC: O(1)
'''

class Solution:
  
'''
1 . for each starting position, set slow and fast pointer
2. continue to advance slow and fast pointer untill slow == fast or the next movement is in the opposite direction
3. if fast == slow check if the length of cycle is greater than 1 return true
4. if fast != slow and we came out of while loop, return false
TC: O(n^2), SC: O(1)
'''

class Solution:
  def getNextIndex(self, arr, current_index, current_direction):
    new_index = (current_index + arr[current_index]) % len(arr)
    if current_index == new_index or arr[new_index] >= 0 != current_direction:
      new_index = -1
    return new_index

  def getIndexNotInSet(self, visited, arr):
    for i in range(len(arr)):
      if i in visited:
        continue
      else:
        return i


  def loopExists(self, arr):
    # write and implement an o(n) algorithm for detecting cycle in this circular array.
    # use the previous visits to each index of arr, if we have visited 
    current_direction = arr[0] >= 0
    current_index = 0
    visited = set()
    while(current_index not in visited):
      if current_index == -1:
        current_index = self.getIndexNotInSet(visited, arr)
        current_direction = arr[current_index] >= 0
      else:
        visited.add(current_index)
      current_index = self.getNextIndex(arr, current_index, current_direction)
    if current_index == -1: # no valid index found tranversing from where we get a valid cycle.
      return False
    return True
