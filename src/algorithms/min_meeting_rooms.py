# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
from heapq import *

#class Meeting:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

# approach 1: search for end time of each interval in the start time of subsequent interval
# approach 2: use binary search to do approach 1 and update the minrooms: O(nlogn)

class Solution:
  def bsearch(self, end, meetings):
    # bsearch end time in start times of meetings indexed from start_id onwards
    low = 0
    high = len(meetings) - 1
    while(low < high):
      mid = low + (high - low) // 2
      if meetings[mid].start < end:
        low = mid + 1
      elif meetings[mid].start > end:
        high = mid - 1
      else:
        return mid
    return low

  def findMinimumMeetingRooms(self, meetings):
    minRooms = 1
    meetings.sort(key = lambda meeting: meeting.start)
    
    for i in range(len(meetings) - 1):
      numRooms = 2 + self.bsearch(meetings[i].end, meetings[i + 1:])
      minRooms = max(minRooms, numRooms)
    return minRooms
