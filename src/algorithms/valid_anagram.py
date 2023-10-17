# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
  def isAnagram(self, s, t):    
    if len(s) != len(t):
      return False
    sMap = {}
    tMap = {}
    for i in range(len(s)):
      if s[i] in sMap.keys():
        sMap[s[i]] += 1
      else:
        sMap[s[i]] = 1                
      if t[i] in tMap.keys():
        tMap[t[i]] += 1  
      else:
        tMap[t[i]] = 1        

    if sMap.keys() == tMap.keys():
      for key in sMap.keys():
        if sMap[key] == tMap[key]:
          continue
        else:
          return False          
      return True      
    else:
      return False      
