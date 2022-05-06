# https://www.interviewbit.com/problems/anagram-match/
'''
1. Clarify
   Q strings A, B
   return Q-sized array with i representing number of sunstrings of A which are anagram of B[i]
2. Min 2 approach

  Input 1:

  A : "jdlidfa"
  B : [ "daf", "ifd", "dxzjbltsmufythgm" ]
  
  Output 1:
  [1, 1, 0]

   BF: TC: O(n^3)
   1. For each string b_i in B: # O(Q)
      1.1. For each sunstring of A: # O(n^2)
        1.1.1. Check isAnagram(A, b_i): if true, result[i] += 1 # O(n)
   2. return result         

   Optimizations:
   1. For each string b_i: check only those substrings of A which have same length as B_i:
      * Run a sliding window of len(B_i) over A and check for anagram between window and B_i  
        * If true update counter

3. Code
def countAnagramSubstrings(A, b_i):
    start = 0
    end = 0
    # create hashmap for B
    hashB = {}
    for letter in b_i:
        hashB[letter] += 1

    while(start+len(b_i) - 1 < len(A)): # across all substrinfgs
        hashA = {}
        for i from 0 to len(b_i): # create hashmap for sliding window
            hashA[A[start + i]] += 1
        # compare hashB with hashA: if matches update counter ese continue            
        if hashA == hashB:
            counter += 1
        else:
            start += 1
    return counter

def solve(self, A, B):
    result = []
    for each b_i in B:
        result.append(self.countAnagramSubstrings(A, b_i))
    return result
            
TC, SC, Edge-cases
'''



class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
