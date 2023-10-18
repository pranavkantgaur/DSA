# https://leetcode.com/problems/happy-number/ 
class Solution:
  
  def getNextNum(self, num):
    num_str = str(num)
    digit_sq_sum = 0
    for digit in num_str:
      digit_sq_sum += pow(int(digit), 2)
    return digit_sq_sum

  def find(self, num):
    slow = num
    fast = self.getNextNum(self.getNextNum(num))

    while(True):
      slow = self.getNextNum(slow)
      fast = self.getNextNum(self.getNextNum(fast))
      if slow == fast:
        break
    return slow == 1              
