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
  
  def getNextId(self, arr, current_id, ref_direction):
    if (arr[current_id] >= 0) != ref_direction:
      return -1

    next_id = (current_id + arr[current_id]) % len(arr)
    if next_id == current_id:
      return -1
    return next_id

  def loopExists(self, arr):
    for i in range(len(arr)):
      slow = i
      fast = i
      ref_direction = arr[i] >= 0
      while(True):
        slow = self.getNextId(arr, slow, ref_direction)
        fast = self.getNextId(arr, fast, ref_direction)
        if fast != -1:
          fast = self.getNextId(arr, fast, ref_direction)
          if fast == slow or fast == -1:
            break
        else:
          break  
      if slow != -1 and slow == fast:
        return True


    return False
