# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
from heapq import *
import heapq

class Solution:
  def rebalanceHeaps(self, min_heap, max_heap):
    if len(max_heap) > len(min_heap) + 1:
      heappush(min_heap, -heappop(max_heap))
    elif len(min_heap) > len(max_heap):
      heappush(max_heap, -heappop(min_heap))

  def getMedian(self, min_heap, max_heap, k):
    if k%2:
      return -max_heap[0] / 1.0
    else:
      return (-max_heap[0] + min_heap[0]) / 2.0  

  def siftUp(self, heap, child_id):
    while(child_id > 0):
      parent_id = (child_id - 1) // 2
      if heap[parent_id] > heap[child_id]: # swap child
        heap[child_id], heap[parent_id] = heap[parent_id], heap[child_id]
      else:
        break # heap property restored.
      child_id = parent_id
    
  def siftDown(self, heap, parent_id):
      while(parent_id < len(heap)):
        child1_id = 2*parent_id + 1
        child2_id = 2*parent_id + 2
        if child2_id < len(heap):
          min_child_id = child1_id if heap[child1_id] < heap[child2_id] else child2_id
          if heap[min_child_id] < heap[parent_id]:
            heap[min_child_id], heap[parent_id] = heap[parent_id], heap[min_child_id]
            parent_id = min_child_id
          else:
            break		
        elif child1_id < len(heap):
          min_child_id = child1_id
          if heap[min_child_id] < heap[parent_id]:
            heap[parent_id], heap[min_child_id] = heap[min_child_id], heap[parent_id]
            parent_id = min_child_id
          else:
            break		
        else: # the current node is a leaf
          break
  
  def addToHeap(self, heap, num):
    # treated as min_heap
    # add the element to the bottom of the heap, i.e. at the last position
    # iteratively sift it up by comaparing its value with that of its parent and then setting the parent as the next children if there was disorder in the current iteration.
    heap.append(num)
    self.siftUp(heap, len(heap) - 1)

  def removeFromHeap(self, heap, num):      
    # treated as min_heap
    id = heap.index(num)    
    heap[id] = heap[-1]
    del heap[-1]
    if id < len(heap):
      # sift up the new element at id 
      self.siftUp(heap, id)
      # sift down
      self.siftDown(heap, id)


  def findSlidingWindowMedian(self, nums, k):
    result = [0.0 for x in range(len(nums) - k + 1)]
    min_heap, max_heap = [], []
    # create min-max heap for first window and add median
    for i in range(k):
      if len(max_heap) == 0 or nums[i] <= -max_heap[0]:
        heappush(max_heap, -nums[i])
      else:
        heappush(min_heap, nums[i])
      self.rebalanceHeaps(min_heap, max_heap)
    result[0] = self.getMedian(min_heap, max_heap, k)

    # update min-max heap for subsequent windows and add median until end of array
    for i in range(1, len(nums) - k + 1): 
      # update the heap, remove arr[i - 1]
      #if -max_heap[0] >= nums[i - 1]: # number is in max_heap
      if -nums[i - 1] in max_heap:                
        self.removeFromHeap(max_heap, -nums[i - 1])            
      else: # number is in min_heap
        self.removeFromHeap(min_heap, nums[i - 1])            
      # rebalance heaps
      self.rebalanceHeaps(min_heap, max_heap)
      # add arr[i + k - 1]
      if nums[i + k - 1] > -max_heap[0]:            
        self.addToHeap(min_heap, nums[i + k - 1])
      else:
        self.addToHeap(max_heap, -nums[i + k - 1])
    # rebalance heaps
      self.rebalanceHeaps(min_heap, max_heap)
    # get the median and update result array
      result[i] = self.getMedian(min_heap, max_heap, k)
    return result
