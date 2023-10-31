# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.


#class job:
#  def __init__(self, start, end, cpu_load):
#    self.start = start
#    self.end = end
#    self.cpuLoad = cpu_load

#  def __lt__(self, other):
#    # min heap based on job.end
#    return self.end < other.end

class Solution:
  def bsearch(self, end, jobs):
    # return -1 if no overlap
    low = 0
    high = len(jobs) - 1
    if end < jobs[0].start:
      return -1     
    while(low < high):
      mid = low + (high - low) // 2
      if jobs[mid].start < end:
        low = mid + 1
      elif jobs[mid].start > end:
        high = mid - 1
      else:
        return mid
    return low


  def findMaxCPULoad(self, jobs):
    max_cpu_load = 0
    jobs.sort(key = lambda job: job.start)
    for i in range(len(jobs) - 1):
      num_overlapp_jobs = 1 + self.bsearch(jobs[i].end, jobs[i+1:]) # if no overlap, bsearch return -1
      cpu_load = jobs[i].cpuLoad
      for j in range(i + 1, i + num_overlapp_jobs):
        cpu_load += jobs[j].cpuLoad
      max_cpu_load = max(max_cpu_load, cpu_load)        
    return max_cpu_load
