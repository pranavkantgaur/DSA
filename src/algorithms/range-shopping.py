'''
# https://www.interviewbit.com/problems/range-shopping/

1. Clarify   
  Input 1:

  A : 
  [
    [1, 2] *
    [4, 2] **
    [3, 2] *
    [4, 3]
  ]
  B : 
  [
    [2, 3, 1, 1] # 2 possibilities of purchase, 1 has min. price = 5
    [1, 4, 2, 1] # X: [1, 2], [3, 4], Y: [4, 2], [4, 3]: Cost: 1 + 3 + 2  + 3 = 9
  ]

  Output 1:

  [5, 9]


2. Min 2 approah
   BF:
   1. Get all possible purchase combinations for given quantities of X and Y # O(nCR, where R = no. of X + no. of Y to be bought, n: number of shops between l and r)
   2. Compute cost of each combination and update min cost # O(1)
   3. return min_cost

   Greedy:
   1. Shops for n X items: Select top n-shops with min. price for X
   2. Select top m-shops with min price for Y from T'(= T - n shops)
   3. Compute cost of selected shops for X and Y and return as min.
3. Code
4. TC, SC, Edge-cases
'''
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
