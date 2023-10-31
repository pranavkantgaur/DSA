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
while(len(min_heap >= 2):  
    if min_heap[0].end < min_heap[1].start:
      result.append(Interval(min_heap[0].end, min_heap[1].start))       
    min_start_time_int = pqpop(min_heap, 0)    
    # get emp id
    emp_id = min_start_time_int.emp_id
    # get next interval for this employee
    int_id = per_emp_int_ids[emp_id]
    if per_emp_int_ids[emp_id] < len(intervals[emp_id]):
      per_emp_int_ids[emp_id] += 1
      pqpush(min_heap, intervals[emp_id][int_id]) # push to heap if possible
return result      
  
  
