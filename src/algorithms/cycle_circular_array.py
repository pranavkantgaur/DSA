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

 '''
1 . for each starting position, set slow and fast pointer
2. continue to advance slow and fast pointer untill slow == fast or the next movement is in the opposite direction
3. if fast == slow check if the length of cycle is greater than 1 return true
4. if fast != slow and we came out of while loop, return false
TC: O(n^2), SC: O(1)
'''

class Solution:
  def get_next_index(self, arr, current_index, current_direction):
    new_index = (current_index + arr[current_index]) % len(arr)
    if current_index == new_index or arr[new_index] >= 0 != current_direction:
      new_index = -1
    return new_index

  def get_index_not_in_set(self, visited, arr):
    for i in range(len(arr)):
      if i in visited:
        continue
      else:
        return i


  def loopExists(self, arr):
    # write and implement an o(n) algorithm for detecting cycle in this circular array.
    # use the previous visits to each index of arr, if we have visited 
    
    for i in range(len(arr)):
      if i in visited:
        continue
      else:
        while(i != -1):
          slow = i
          fast = i
          visited.add(i)
          while(True):
            slow = self.get_next_index()
            fast = self.get_next_index()
            if fast != -1:
              fast = self.get_next_index()
              if slow == fast or fast == -1:
                break
              else:
                visited.add(fast)
