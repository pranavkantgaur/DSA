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

  def loopExists(self, arr):
    # write and implement an o(n) algorithm for detecting cycle in this circular array.
    # use the previous visits to each index of arr, if we have visited 
    # assuming that i need to keep previously visited indices and indices visited in current traversal separate
    current_direction = arr[0] >= 0
    current_index = 0
    prev_visited = set()

    for i in range(len(arr)):
      if i in prev_visited:
        continue
      else:
        current_visited = set()
        ptr = i
        current_visited.add(i)
        while(True):
          new_ptr = self.get_next_index(arr, ptr, current_direction)
          if new_ptr == -1:
            prev_visited.update(current_visited)
            break
          if new_ptr in current_visited: # will not be visiting an index already visited for previous i
            return True
          else:
            if new_ptr in prev_visited:
              prev_visited.update(current_visited)
              break
            else:
              current_visited.add(new_ptr)
            # how to differentiate between indices visited in the past and indices we are visiting in current cycle?
    return False      
