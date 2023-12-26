# You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.

from heapq import *

class Solution:
  def scheduleTasks(self, tasks, k):
    # create task freq. counter
    task_freq_ctr = {}
    for task in tasks:
      if task in task_freq_ctr:
          task_freq_ctr[task] += 1
      else:
          task_freq_ctr[task] = 1 
    # push task ids to a max-heap, prioritizing tasks with highest frequency, WHY? expected to strech the time-line the most, so lets start them first
    max_heap = []
    result = []
    for task_id in task_freq_ctr:
      heappush(max_heap, (-task_freq_ctr[task_id], task_id)) 
    # enter a loop untill heap is not empty:
    while(len(max_heap)): 
      # take out most freq. task:
      _, task1_id = heappop(max_heap) # A
    # update its freq. in counter map
      task_freq_ctr[task1_id] -= 1 
    # append its id to the result
      result.append(task1_id) 
    # check if task needs to be scheduled again in future?
      if task_freq_ctr[task1_id]:  
        # in a loop of size k - 1
        interm_task_ctr = 0
        tasks_taken_out_queue = [task1_id] # to make sure that the current most freq. task is schduled as the first again(avoids cooling period violation for same freq. tasks)
        while(interm_task_ctr <= k - 1): 
          # untill heap is not empty:
          if len(max_heap): 
            # take out tasks from the heap
            _, task2_id = heappop(max_heap) 
            # update task freq. counter
            task_freq_ctr[task2_id] -= 1 
            # append it to the result
            result.append(task2_id) 
            # add it to the tasks taken out set if its current freq. is > 0
            if task_freq_ctr[task2_id]:
                tasks_taken_out_queue.append(task2_id) 
          # if heap is empty:
          else:
            # continue with pushing idle task to the result
            result.append('#')
          interm_task_ctr += 1
        # add all tasks back to the heap along with the first task 
        while(len(tasks_taken_out_queue)):
          task_id = tasks_taken_out_queue.pop(0)
          heappush(max_heap, (-task_freq_ctr[task_id], task_id)) 
      else: # no taks needs to be resceduled again, so the cooling period does not matter anymore.
        while(len(max_heap)): 
          result.append(heappop(max_heap)[1]) 
        break
    return len(result)
