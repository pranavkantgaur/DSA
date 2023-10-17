# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

class Solution:
  
  def getNextIndex(self, sub_str):
    hash_counter = 0
    ptr = len(sub_str) - 1
    while(ptr >= 0):
      if sub_str[ptr] == '#':
        hash_counter += 1
        ptr -= 1
      else:
        break        
    return hash_counter * 2

  def compare(self, str1, str2): # s1 = xy#z, s2 = xzz#
    ptr1 = len(str1) - 1 # p1 = z, p2 = #
    ptr2 = len(str2) - 1
    while(ptr1 >= 0 and ptr2 >= 0):
      ptr1 -= self.getNextIndex(str1[:ptr1 + 1])
      ptr2 -= self.getNextIndex(str2[:ptr2 + 1]) 
      if ptr1 >= 0 and ptr2 >= 0 and str1[ptr1] != str2[ptr2]:
        return False
      elif ptr1 >= 0 ^ ptr2 >= 0:
        return False              
      else:
        ptr1 -= 1
        ptr2 -= 1
    return True
