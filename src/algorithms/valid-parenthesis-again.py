# https://www.interviewbit.com/problems/valid-parentheses-again/

'''
1. Clarify
   1. X +Y is valid seq. '+' is concat?
   2. Length % 2 == 0
2. Min 2 approaches:
   Input 1: Output 1:   3
   A = "??}(??" -> 3 *   # 6 possib. per pos., unconstrained., # max. no. 6 * no. of ?
   [{}()], ({}()), {{}()}-> because, given letters } and length of left substring(2) implied that A[1] = '{'
   similarly, A[3] = '(' and len(A[4:]) impoied A[5] = ')', therefore, only A[0] and A[-1] were left and 
   since inner substring is valid, we can use rule-2(in desc.) to have 3 valid combinations.
   For each given letter in input string, the number of valid combinations reduce by factor of 6: 
   T = len-times 6 / (6 * 2 * no. of given letters) = 6 * 6 * 6 * 6 * 6 * 6/ 6 * 6 * 6 * 6 = 36 (for A[0] and A[-1])
   But A[0] and A[-1] are constrained to have 3 combinations only.

   Start from letters already present in string and try to count valid combinations which could be constructed.

   Recursive:
   if len(A) is None: count *= 1
   if isValid(X) and A[X-1] == '?' and A[X+ 1] == '?' then count *= 3
   if isValid(X) and isValid(Y) then count *= 1
   


3. Code
4. TC, SC, edge-cases
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
