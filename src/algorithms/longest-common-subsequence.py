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
1. For each char in s2 mark all positions where it occurs in s1, if none then increment s2 char pointer
2. if char is found a n positon in s1: parallely check remaining letters of s2 in following substring in s1(wrt all position marked in step-1)
3. TODO


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

More TODO

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
