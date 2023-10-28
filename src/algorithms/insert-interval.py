# https://leetcode.com/problems/insert-interval/
#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

'''
1. binary search input interval in the intervals
2. for left-new-right interval scenario:
   1. check and insert based on the case:
        if left and right are valid:
          if new.start <= left.end:
            if new.end > right.start:
              merge left-new-right
            else:
              merge left-new
        else:
            if new.end > right.start:
              merge new-right
            else:
              insert new between left and right    
  2. elif left is valid:
     if new.end > left.start:
      merge new-left
     else:
      insert new before left 
  3. else: # right is valid and left does not exist
      if new.start < right.end:
        merge right-new
      else:
        insert new after right
  4. iterate on following intervals:
     * ignore them if last_inserted_interval.end > new_int.end
     * if not so, then check if last_interval.end >= new.start: update end of last_int
     * else: insert new interval = new
  5. directly insert all following intervals
  6. return intervals
'''

class Solution:
  
  def bsearch(self, intervals, new_interval):
    
    if new_interval.start <= intervals[0].start:
      return -1
    left = 0
    right = len(intervals) - 1
    while(left < right):
      mid = left + (right - left) // 2
      if intervals[mid].start > new_interval.start:
        right = mid - 1
      elif intervals[mid].start < new_interval.start:
        left = mid + 1
      else:
        left = mid
        break
    return left

  def insert(self, intervals, new_interval):
    merged = []
    # bsearch insert location
    start_left = self.bsearch(intervals, new_interval)
    if start_left != -1:
      # append all intervals on the left
      for i in range(start_left):
        merged.append(intervals[i])

      if new_interval.start <= intervals[start_left].end:
        start = intervals[start_left].start
        end = max(new_interval.end, intervals[start_left].end)
      else:  
        merged.append(intervals[start_left])
        start = new_interval.start
        end = new_interval.end
      next_check_id = start_left + 1
    else:
      start = new_interval.start
      if new_interval.end >= intervals[0].start:
        end = max(new_interval.end, intervals[0].end)
        next_check_id = 1
      else:
        end = new_interval.end
        next_check_id = 0

    while(next_check_id < len(intervals)):
      if end >= intervals[next_check_id].start:
        end = max(end, intervals[next_check_id].end) # merge upcoming interval
        next_check_id += 1
      else:
        break
    merged.append(Interval(start, end))
    next_insert_id = next_check_id
    while(next_insert_id < len(intervals)):
      merged.append(intervals[next_insert_id])
      next_insert_id += 1  
    
    return merged
