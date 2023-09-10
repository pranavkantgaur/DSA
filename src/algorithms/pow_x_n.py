'''
[2.0, 10] -> 1024.0

[2.1, 3] -> 9.26

[2.0, -2] -> 0.25

Clarify:
1. Pow could be negative, fraction?
2. X could be float? 

Naive: 
1. Multiple X n number of times. How to apply this for fractional n? Fractional n not allowed.

Another approach:
1. If n is even, n/2 multiplications of numbers then take a square -> TC: O(logn)
2. If n is odd: n - 1 / 2 multiplications of numbers * square of n - 1/2 multiplications * x

TC: O(logn) ?, SC : O(logn) [number of recursive calls active at a moment]
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: 
            return 1        
        else:
            if n % 2 == 0:
                k = self.myPow(x, n / 2)
                res = k * k
            else:
                k = self.myPow(x, (n - 1) / 2)
                res = k * k * x
            return res
        
'''
