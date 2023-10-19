# https://leetcode.com/problems/circular-array-loop/description/
'''
1 . for each starting position, set slow and fast pointer
2. continue to advance slow and fast pointer untill slow == fast or the next movement is in the opposite direction
3. if fast == slow check if the length of cycle is greater than 1 return true
4. if fast != slow and we came out of while loop, return false
TC: O(n^2), SC: O(1)
'''

class Solution:
  
  
  def getCurrentDirection(self, arr, slow):
    return arr[slow] > 0
  
  def getNextId(self, arr, current_id):
    #next_id = current_id % (len(arr) - 1)
    next_id = (current_id + arr[current_id]) % len(arr)
    return next_id

  def loopExists(self, arr):
    for i in range(len(arr)):
      slow = i
      fast = i
      ref_direction = self.getCurrentDirection(arr, slow)
      while(True):
        next_slow = self.getNextId(arr, slow)
        if next_slow == slow:
          break
        if self.getCurrentDirection(arr, next_slow) == ref_direction:
          slow = next_slow
          fast = self.getNextId(arr, self.getNextId(arr, fast))
          if slow == fast and slow != self.getNextId(arr, fast):
            return True
        else:
          break

    return False
