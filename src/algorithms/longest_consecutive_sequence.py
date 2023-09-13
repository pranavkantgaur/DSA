'''
# https://leetcode.com/problems/longest-consecutive-sequence/
Clarify:
1. Possible to not to have anmy solution? No

Naive algorithm:TC: O(nlogn), SC: O(1)
1. Sort the array
2. Find out the consecutive subarrays:
   1. Check the difference of succesive numbers, if it is 1, then set the start pointer to the current number
   2. Continue to increment the end pointer untill the difference between successive numbers is 1
   3. Once the condition violates, update the max_length_consecutive_sequence
   4. Go to 1,untill end of array is not reached by end pointer.
3. Return the length of the longest subaray

def func(arr):
  arr = sorted(arr)	
  max_len = -1
  start = 0
  end = 0   
  i = 0  
   while(end < len(arr)):
    while(nums[i+1] - nums[i] == 1):
      end += 1
      i += 1
    if max_len < end - start:
      max_len = end - start
    i += 1
    start = i # reset start and end
    end = i	
* Forum solution: https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak/ , TC-> O(n), SC: O(n)
  1. Convert input into a set
  2. Start with the first element, y of the set and check if y+1, y+2... is there, once we find a number not present in the set, we update the end number for this sequence, do the same for start number by looking for y-1, y-2.
  3. Once both start and end are found, update the global max and remove the numbers from the set
  4. Repeat from 1.
  Implementation:
  def get_longest_seq(nums):
    nums_set = set(nums)
    for num in nums_set:
      while(right_ele in nums_set):
        id = nums_set.get_id(right_ele)
        len += 1
        nums_set.remove(id)
        
      while(left_ele in nums_set):
        len += 1
        id = nums_set.get_id(left_ele)
        nums_set.remove(id)
      
      if len > max_len:
        max_len = len
    return max_len      
'''
