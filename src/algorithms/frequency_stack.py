from heapq import *
# Design a class that simulates a Stack data structure, implementing the following two operations:
# push(int num): Pushes the number ‘num’ on the stack.
# pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.


class Item():
  def __init__(self, num, frequency, sequence_number):
    self.frequency = frequency
    self.sequence_number = sequence_number
    self.num = num
  def __lt__(self, other):
    if self.frequency < other.frequency: return False
    if self.frequency > other.frequency: return True      
    return self.sequence_number > other.sequence_number


class Solution:
  def __init__(self):
    self.letter_counter = {}
    self.max_heap = []
    self.sequence_num = 0

  def push(self, num): # 15
    if num in self.letter_counter:
        self.letter_counter[num] += 1 # h: [10:0, 15:1]
    else:
        self.letter_counter[num] = 1 # h: [10:1, 15:1]
    item = Item(num, self.letter_counter[num], self.sequence_num) # (15, 1, s4)
    heappush(self.max_heap, item) # heap: [[15, 1, s3]]
    self.sequence_num += 1 # s: s5
      
  def pop(self):
    if len(self.max_heap): # 0
        self.letter_counter[self.max_heap[0].num] -= 1 # h: [10:0, 15:0]
        return heappop(self.max_heap).num # heap: []
    else:
        return None

