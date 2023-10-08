# https://leetcode.com/problems/ones-and-zeroes/
# Counter example for suboptimal value/ weight greedy strategy: https://cs.stackexchange.com/a/141289
# It seems that in general, if the v/w values are close and selecting based on v/w results in weight quota wastage then that will be a counter example.
class Solution:
    

    def get_01_count(self, str):
        l_1, l_2 = 0, 0
        for letter in str:
            if letter == '0':
                l_1 += 1
            if letter == '1':
                l_2 += 1
        return l_1, l_2            

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        1. start with smallest strings for accumalate
        2. take no take approach
        pseudo:
        base:
        1. if len of strs is 1: return 1 if num of 0,1 are <= m, n, else return 0
        2. if m == 0 and n == 0: return 0
        recurse:
        1. take first string by recurse call and pass the updated strs, m, n
        2. receive the subset len possible, l_1
        3. no take first string, by recurse call and pass the updates strs, old m, n
        4. get l_2
        5. return max(l_1, l_2)
        TC: O(m * 2^n), SC: O(n)

        Approach 2:
        Using memoization:
        1. Create an array with size: [length of string array][m][n], set each cell to 0
        2. For each base case, set corresponding array value
        3. For recurse case, check if value of subproblem is already computed, then set the solution value of current problem in the array and return.
        '''
        '''
        if len(strs) == 1:
            l_1, l_2 = self.get_01_count(strs[0])
            if  l_1 <= m and l_2 <= n:
                return 1
            else:
                return 0
        if m <= 0 and n <= 0:
            return 0
        
        # no take                
        l_2 = self.findMaxForm(strs[1:], m, n)

        # take
        m1, n1 = self.get_01_count(strs[0])
        if m1 > m or n1 > n:
            l_1 = 0        
        else:
            m -= m1
            n -= n1
            l_1 = 1 + self.findMaxForm(strs[1:], m, n)
        
        return max(l_1, l_2)
        '''
        dp = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(len(strs))]        
        return self.helper(strs, m,n, dp) 

    def helper(self, strs, m, n, dp):
        # base 
        if len(strs) == 1:
            m1, n1 = self.get_01_count(strs[0])
            if m1 <= m and n1 <= n:
                dp[len(strs) - 1][m - 1][n - 1] = 1
                return 1
            else:
                return 0    
        if m == 0 and n == 0:
            dp[len(strs) - 1][m][n] = 0
            return 0        
        # no take
        m1, n1 = self.get_01_count(strs[0])        
        if dp[len(strs) - 2][m - 1][n - 1] != -1: # no take recurse is already solved?            
            if m1 > m or n1 > n:
                dp[len(strs) - 1][m - 1][n - 1] = dp[len(strs) - 2][m - 1][n - 1]
            else:    
                if dp[len(strs) - 2][m - m1 - 1][n - n1 - 1] == -1: # take recurse if not already solved?
                    dp[len(strs) - 2][m - m1 - 1][n - n1 - 1] = self.helper(strs[1:], m - m1, n - n1, dp)
                dp[len(strs) - 1][m - 1][n - 1] = max(dp[len(strs) - 2][m - 1][n - 1], 1 + dp[len(strs) - 2][m - m1 - 1][n - n1 - 1])
                           
        else:
            dp[len(strs) - 2][m - 1][n - 1] = self.helper(strs[1:], m, n, dp) # solve no take recurse
            if m < m1 or n < n1:
                dp[len(strs) - 1][m - 1][n - 1] = dp[len(strs) - 2][m - 1][n - 1]
            else:    
                #print('A: ', len(strs) - 2, m - m1, n - n1)
                if dp[len(strs) - 2][m - m1 - 1][n - n1 - 1] == -1: # take recurse if already solved? 
                    dp[len(strs) - 2][m - m1 - 1][n - n1 - 1] = self.helper(strs[1:], m - m1, n - n1, dp)
                dp[len(strs) - 1][m - 1][n - 1] = max(dp[len(strs) - 2][m - 1][n - 1], 1 + dp[len(strs) - 2][m - m1 - 1][n - n1  -1])                         
        
        return dp[len(strs) - 1][m - 1][n - 1]     
