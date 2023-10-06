# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        current = 0
        i = 0
        first_candidate = -1
        len_needle = len(needle)
        len_haystack = len(haystack)
        while(current < len_haystack):
            if haystack[current] == needle[i]:
                if haystack[current] == needle[0] and first_candidate == -1:
                    first_candidate = current
                i+=1                
                if i == len_needle:
                    return current - len(needle) + 1               
            else:
                i = 0     
                if first_candidate != -1:
                    current = first_candidate
                    first_candidate = -1
                if current + len_needle > len_haystack:
                    return -1                    
            current +=1                
        return -1     
        '''
        * For overlapping substrings if one of them contains needle then with above approach it will miss it.
        * I should move the left pointer to the next starting letter instead of skipping the previously mismatched substring altogether.
        '''                 
