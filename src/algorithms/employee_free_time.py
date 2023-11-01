# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.
import heapq

#
#class Interval:
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end
#
#    def print_interval(self):
#        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')
#

class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start

class Solution:
  def findEmployeeFreeTime(self, schedule):
      result = [] 
      current_int_index_list = [0 for _ in range(len(schedule))]   # points to the index of the current interval for each employee which is in the heap
      min_heap = []
      for i in range(len(schedule)):
        item = (schedule[i][0].start, [schedule[i][0], i])
        heapq.heappush(min_heap, item)
      prev = min_heap[0].interval
      while(min_heap):
        top = heappop(min_heap)
        if top.start > prev.end:
          result.append(Interval(orev.end, top.start))
          prev = top
        else:
          if top.end > prev.end:
            prev = top
        
        next_int_id = current_int_id + 1
        if next_int_id < len(schedule[empId]):
          next_int = schedule[empId][next_int_id]
          heappush(min_heap, next_int)

      return result                  
