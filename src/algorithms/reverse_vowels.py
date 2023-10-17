# Given a string s, reverse only all the vowels in the string and return it.
class Solution:
  def reverseVowels(self, s: str) -> str:
    left = 0
    right = len(s) - 1
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    s_list = list(s)
    while(left < right):
      while(left < right and s_list[left].lower() not in vowel_list):
        left += 1
      while(left < right and s_list[right].lower() not in vowel_list): 
        right -= 1
      
      if left != right:
        t = s_list[left]
        s_list[left] = s_list[right]
        s_list[right] = t               
              
      left += 1
      right -= 1  

    s = ""
    for letter in s_list:
      s += letter
      
    return s
