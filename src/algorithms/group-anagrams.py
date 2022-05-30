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
        for index, string in enumerate(strs):
            result = []
            candidate_index = index + 1
            while(candidate_index <= len(strs) - 1 and \
                  len(string) == len(strs[candidate_index])):
                if self.isAnagram(string, strs[candidate_index]):
                    result.append(strs[candidate_index])
                    strs.remove(strs[candidate_index])
                else:
                    candidate_index += 1
            result.append(string)                        
            results.append(result)                    
        return results            
