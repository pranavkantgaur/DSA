# https://leetcode.com/problems/merge-intervals/

#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
  def merge(self, intervals):
    mergedIntervals = []
    intervals.sort(key = lambda inter: inter.start)
    mergedIntervals.append(intervals[0])
    for idx in range(1, len(intervals)):
      if intervals[idx].start <= mergedIntervals[-1].end:
        new_interval = Interval(mergedIntervals[-1].start, max(intervals[idx].end, mergedIntervals[-1].end))
        mergedIntervals.pop(-1)
        mergedIntervals.append(new_interval)
      else:
        mergedIntervals.append(intervals[idx])
    return mergedIntervals
