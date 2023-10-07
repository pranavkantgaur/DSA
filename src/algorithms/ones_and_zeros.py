# https://leetcode.com/problems/ones-and-zeroes/
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
        
