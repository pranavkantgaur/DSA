# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
  def canAttendAllAppointments(self, intervals):
    intervals.sort(key = lambda interv: interv.start)    
    for i in range(1, len(intervals)):
      if intervals[i].start > intervals[i - 1].end:
        continue
      else:
        return False 
    return True
