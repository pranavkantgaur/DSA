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
    # 1. for each interval in b, i_b:
    # 2. for each interval in a, i_a:
    # 3. check if i_b intersects with i_a: anything apart from a-b or b-a is intersection.
    # 4. if yes, start = max(i_a.start, i_b.start), end = min(i_a.end, i_b.end)
    # 5. insert new interval into the result list
    # 6. if not, then skip i_a   
    # with binary search the TC becomes O(nlogn)
    for i_a in range(len(intervals_a)):
      for i_b in range(len(intervals_b)):
        if self.interv_intersect(intervals_a[i_a], intervals_b[i_b]):
          start = max(intervals_a[i_a].start, intervals_b[i_b].start)
          end = min(intervals_a[i_a].end, intervals_b[i_b].end)
          result.append(Interval(start, end))
        else:
          continue
    return result
