# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
  def interv_intersect(self, i_a, i_b):
    return not (i_a.end < i_b.start or i_b.end < i_a.start)

  def merge(self, intervals_a, intervals_b):
    result = []
    last_ib = 0
    for i_a in range(len(intervals_a)):
      i_b = last_ib
      intersection_found = False
      while(i_b < len(intervals_b)):
        if self.interv_intersect(intervals_a[i_a], intervals_b[i_b]):
          start = max(intervals_a[i_a].start, intervals_b[i_b].start)
          end = min(intervals_a[i_a].end, intervals_b[i_b].end)
          result.append(Interval(start, end))
          last_ib = i_b
          intersection_found = True
        else:
          if intersection_found == True:
            break
        i_b += 1
    return result
