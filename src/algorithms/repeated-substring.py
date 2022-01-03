'''
Input: s = "abab"
Output: true

Input: s = "aba"
Output: false

Input: s = "abcabcabcabc"
Output: true

1. Questions:
   1. types of chars allowed
   2. if string length is odd, avoid substrings of even length
   3. result substring must start from s[0] ?
   4. if string length is even, consider odd length substrings as well
2. BF solutuon: O(n substrings each starting from s[0] * n comparisons) = O(n^2)
   2.0. if lentgth of string is odd, avoid n / 2 even length sunstrings.
   2.1. For each substring:
        2.1.1 Check if repetiton of length n = input string
              If true return true else continue:
   
'''
class Solution:    
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        for substrLength in range(1, len(s) // 2 + 1): # 1, 2       
            if not len(s) % substrLength: 
                hasSubstringRepetition = False
                for left in range(substrLength, len(s) - substrLength + 1, substrLength): # 1, 3
                    if s[:substrLength] == s[left: left + substrLength]:                                        
                        hasSubstringRepetition = True
                        continue
                    else:
                        hasSubstringRepetition = False
                        break
                    
                if hasSubstringRepetition:
                    return True
            else:
                continue
            
        return False    
    
        
