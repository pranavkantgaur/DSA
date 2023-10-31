# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.
'''
Approach: using min-heap, TC: O(n*logk) SC: O(k) ,  better than sorting all intervals as a whole and checking for gaps (O(nlogn))
1. create a list of indices across all emplyee intervals, per_emp_int_ids = [], init will list of k zeros
2. create a min heap storing the intervals of each employee pointed to by the corresponding entry in per_emp_int_ids
3. in a loop, untill min_heap is not empty: 
   * check if min_heap[0].end < min_heap[1].start: new_interval_start = min_heap[0].end, new_interval_end = min_heap[1].start, result.append(Interval(new_interval_start, new_interval_end))
   * else: do nothing
   * remove top element from heap(regardless of prev. if/else), get corresponding emp_id, push next interval of that employee using per_emp_int_ids[emp_id] value    
4. return result   
'''
from heapq import *

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
      next_int_index_list = [0 for k in range(len(schedule))]   
      min_heap = []
      for i in range(len(schedule)):
        heapq.push(min_heap, [schedule[i][0], i])

      while(len(min_heap) >= 2):
        if min_heap[0].end < min_heap[1].start:
          result.append(Interval(min_heap[0].end, min_heap[1].start))
        # remove the earliest start time interval from heap
        min_start_inter = heap.pop(min_heap) # TODO: check heap API
        # insert nxt interval for same employee in the heap
        emp_id = min_start_int[1]
        next_inter_id = next_int_index_list[emp_id]
        if next_id < len(schedule[emp_id]):
          heap.push([schedule[emp_id][next_id], emp_id])
          next_int_index_list[emp_id] += 1          
      return result                  


      return result
     
  
  
