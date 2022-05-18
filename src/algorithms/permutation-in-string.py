'''
# https://leetcode.com/problems/permutation-in-string
Approach 1:
0. Create hashmap of s1 with count of each letter
1. Create sliding window of length = len(s1)
2. Slide the window over s1:
   2.1. Set hashmap/counter of alphbets in each substring of s1 of length = len(s1)
   2.2. Compare the hashmap with that of s2: 
        2.2.1. If found, return true
        2.2.2. Else continue untill all substrings are checked
   2.3. return FALSE        
TC: O(n)
SC: O(1)

Optimization:
1. Compute hashmap for first substring only(O(n))
2. For later substrings, just update the hashmap(O(1)): h[s2[start]] -= 1 , if end + 1 < len(s2): h[s2[end + 1]] += 1, start += 1, end += 1
Approach 3: (recursive):

'''
import string
class Solution:        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False        
        hMapS1 = dict.fromkeys(string.ascii_lowercase, 0)
        hMapS2 = dict.fromkeys(string.ascii_lowercase, 0)
        for letter in s1:
            hMapS1[letter] += 1        
        start = 0
        end = len(s1) - 1
        temp = start
        # initililizing hashmap for s2 substring(within sliding window)
        temp = start                        
        while(temp <= end):
            hMapS2[s2[temp]] += 1
            temp += 1        
        while(end < len(s2)):        
            # compare if hashmaps match            
            if hMapS1 == hMapS2:
                return True
            else:
                hMapS2[s2[start]] -= 1
                if end + 1 < len(s2):
                    hMapS2[s2[end + 1]] += 1
                start += 1
                end += 1                
        return False                
        
