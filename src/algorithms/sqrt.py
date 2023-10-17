# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.


import math

class Solution:
  def mySqrt(self, x: int) -> int:
    # TODO: Write your code here
    left = 1
    right = x
    while(left <= right):
      mid = left + (right - left) // 2 # m = 2
      n_app = mid * mid # n = 4
      if n_app < x:
        left = mid + 1 # l = 2
      if n_app > x:
        right = mid - 1 # r = 3, l = 1
      else:
        return mid  
    return left
