# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
  def updatePointers(self, s, left, right):
    while(left < len(s) and not s[left].isalnum()):
      left += 1
    while(right > -1 and not s[right].isalnum()):
      right -= 1
    return left, right

  def isPalindrome(self, s: str) -> bool:
    if len(s) == 1:
      return True      
    left = 0
    right = len(s) - 1
    left, right = self.updatePointers(s, left, right)
    while(left < right):
      if s[left].lower() == s[right].lower():            
          left, right = self.updatePointers(s, left + 1, right - 1)
      else:
        return False          
    return True
