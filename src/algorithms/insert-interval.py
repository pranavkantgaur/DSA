# https://leetcode.com/problems/insert-interval/
#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
  def insert(self, intervals, new_interval):
    merged = []
    start = new_interval.start
    end = new_interval.end
    is_inserted = False
    for i  in range(len(intervals)):
      if intervals[i].end < start:
        merged.append(intervals[i])
      else: # interval.end >= start
        if intervals[i].start <= end:
          start = min(start, intervals[i].start)
          end = max(end, intervals[i].end)
          is_inserted = False
        else: 
          if not is_inserted:
            merged.append(Interval(start, end))
            is_inserted = True
          merged.append(intervals[i])
    if not is_inserted:
      merged.append(Interval(start, end))

    return merged
