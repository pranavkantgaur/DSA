# https://leetcode.com/problems/happy-number/
class Solution:
  
  def getNextNum(self, num):
    num_str = str(num)
    digit_sq_sum = 0
    for digit in num_str:
      digit_sq_sum += pow(int(digit), 2)
    return digit_sq_sum

  def find(self, num):
    # TODO: Write your code here
    slow = num
    fast = self.getNextNum(self.getNextNum(num))
    while(slow != fast):
      slow = self.getNextNum(slow)
      fast = self.getNextNum(self.getNextNum(fast))
      if slow == fast:
        if slow == 1:
          return True
        else:
          return False               
    if slow == 1:
      return True
    else:
      return False                
