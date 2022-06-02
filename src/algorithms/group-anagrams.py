# https://leetcode.com/problems/group-anagrams/
'''
Appraoch 1 : TC: O(n^2), TC: O(n)
1. Sort strings based on lengths
2. For each string in resulting array:
   2.1. Search for anagrams within subarray of same length strings
   2.2. For each match, remove the string from array and add to the result list
   2.3. Continue untill all strings(in sub-array) are compared, post that, 
        add compared string to the result list, increment start string pointer
        and reinit result list
         
'''
from collections import Counter

class Solution:
    def isAnagram(self, str1, str2):
        return Counter(str1) == Counter(str2)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        strs = sorted(strs, key=len) # sort based on length
        print("str", strs)
        visited = [False for string in strs]
        for index, string in enumerate(strs):
            if not visited[index]:
                visited[index] = True
                result = []
                candidate_index = index + 1
                while(candidate_index <= len(strs) - 1 and \
                  len(string) == len(strs[candidate_index])):
                    if self.isAnagram(string, strs[candidate_index]):
                        result.append(strs[candidate_index])
                        visited[candidate_index] = True
                        #strs.remove(strs[candidate_index])
                    candidate_index += 1                                            
                result.append(string)                        
                results.append(result)   
            else:
                continue          
                 
        return results            
   
   def computeSortedString(word):
      '''
      sortedWord = [letter for letter]
      '''
   # based on hashmap of lists of strings
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # init hashmap
      stringHMap = {}
      # for each string in input
      for words in strs:
         # set key = corresponding sorted string
         key = sorted(word)
         stringHMap[key].append(word)
     # return values of the resulting hashmap 
     return stringHMap.values()
      
