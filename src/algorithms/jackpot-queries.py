# https://www.interviewbit.com/problems/jackpot-queries/
'''
1. Calrify problem:
   1.1. Data, assumptions, dataformat:
        1 operatio: T = T - M + X xor Y or T = X xor Y
        A: List/Bag of N ints , could repeat? could draw same item twice?
        B: Price list for Q items
        O/P: String as '011000...Q size'
2. Discuss min 2 approaches
   A = [1, 2], B = [3, 5, 10, 15]
   [01 xor 10 = 11(3)] -> 1 -> 0 -> 
   O/P: "1001"
   
   BF:
   0. Check if an item can be purchased:(A, cost):
      0.1. For each combination of 2 numbers, X, Y in A: # for x in A: for y in A:
           0.1.1. Check if X xor Y == cost:
                  return true
           0.1.2. Else continue                         
      
   1.  For each item:
       1.1. Check if it can be purchased by any number of operations            
            1.1.1 if yes, append 1 to result else 0
    
3. Explain while coding
4. Write compilable, modular, readable code
5. Brainstorm edge-cases
'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a strings
    def solve(self, A, B):
