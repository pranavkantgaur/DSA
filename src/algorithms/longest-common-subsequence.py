# https://leetcode.com/problems/longest-common-subsequence/
'''
BF:
0. Set lcs_len = 0
1. For each string s1 and s2, list their subsequences, in lists, sub1, sub2 --- O(max(2^m, 2^n))
   1.1. List s1 subsequences: 
        1.1.1. For each of the 2^{len(s1)} combinations of missing chars: generate SubSequence and append to sub1
          1.1.1.1.     
   1.2. List s2 subsequences:
        1.2.1. For each of the 2^{len(s2)} combinations of missing chars: generate SubSequence and append to sub2
        
2. For each subsequence in sub1 find matching subsequence in sub2
   2.1. If a match is found, update the lcs_len if length of subseuence is greater than the value of lcs_len, 
   2. if match is not found, continue
3. return lcs_len   
TC: O(max(2^m, 2^n))
SC: O(1)


Iterative string matching:
0. current_substrings = [s1], substrings_with_l = [], lcs = []
1. For each letter l in s2:
   1.0. for all substrings in current_substrings, which contain l:
        1.1. update current_substrings = getNewSubstrings(l, current_substrings)
        1.2. Append l to current lcs
2. For next letter till the last: (TODO)
   if letter is found at index before the stating position of previous lcs candidates:
      Do above acitviity again and update lcs candidate if length is greater
3. Return length of lcs


Optimization:
1. If a subsequence of length n, s_n is known to be common among s1 and s2, then we need not check for it again while
  checking for all subsequrnces of form s_n+1 = s_n(already matching) + one_char, here only check if one_char lies in the remaining
  strings s1[lastIdOfS1(s_n) + 1:] and s2[lastIdOfS2(s_n) + 1:]
  lcs(s1[:i+1], s2[:j+1]) = max_length_sequence_among(lcs(s1[:i], s[:j+1]), lcs(s1[:i + 1], s[:j]), lcs(s1[:i], s[:j]))
  
List test cases:
Input: text1 = "abcde", text2 = "ace" 
Output: 3 

Input: text1 = "abc", text2 = "abc"
Output: 3

Input: text1 = "abc", text2 = "def"
Output: 0

Input: text1 = "abcde", text2 = "acer" 
Output: 3 

Input: text1 = "abcde", text2 = "cer" # ce is lcs
Output: 2 



More TODO, test cases with multiple common and disjoint(not like subsets of each other) subsequences

'''
class Solution:
    def getIndexOfLetter(self, letter, substring):
        # https://stackoverflow.com/a/11122355
        return [i for i, ltr in enumerate(substring) if ltr == letter]
        
    def getNewSubstrings(self, letter, matching_substring):
        new_substrings = []
        letter_indices = self.getIndexOfLetter(letter, matching_substring)            

        for index in letter_indices:
            new_substrings.append(matching_substring[index + 1:])
        return new_substrings                
    
    def getMatchingSubstrings(self, letter, current_substrings):
        matching_substrings = []
        for substring in current_substrings:
            if letter in substring:
                matching_substrings.append(substring)
        return matching_substrings
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        current_substrings = [text1]
        lcs = []
        for letter in text2:
            new_substrings = []
            matching_substrings = self.getMatchingSubstrings(letter, current_substrings) # all substrings containing letter      
            for substring in matching_substrings:
                new_substrings.append(self.getNewSubstrings(letter, substring))
            if len(matching_substrings): # if there was a match, we must iterate on the resulting substrings
                current_substrings = new_substrings[0]                         
                lcs.append(letter)                
        return len(lcs)                        
