'''
1. Set TL = [0,0], TR=[0, m-1], BL = [n - 1, 0], BR=[n-1, m-1]
2. For i from 1 to X:
   2.0  Set seed from i 
   2.1. Print from TL + seed_x to TR - seed_x 
   2.2. Print from TR + seed_y  to BR - seed_y 
   2.3. Print from BR - seed_x to BL - seed_x 
   2.4. Print from BL - seed_Y to TR - seed_Y 
   
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
