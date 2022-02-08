'''
https://leetcode.com/problems/container-with-most-water/

My understanding:

    I start with biggest width, left = 0, right = n - 1
    Compute water with this left and right
    Now in order to explore other pairs/solutions, we have to update either our left or right pointer:

    lets assume left is smaller, but instead of updating left I decrement my right: You will notice that the area of the resulting container is bound to be smaller than that of previous [left-right] container
    So, I must increment left in this case, same logic applies for the right pointer
    Once I have updated my left/right pointer in this iteration, I repeat the process
    Since in each iteration, left and right pointers come closer by 1, time complexity is O(n)
    
How we arrive at this from brute-force?    
this O(n) starts with a reasonable choice of left and right pointers(max width) and then for an index(say left) avoids exploring hopeless combinations of [left, right]
that way it is an optimization over the naive approach

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)  - 1
        maxc_water = system.intmin
        while(right > left):
            water = min(height[left], height[right]) * (right - left)
            if water > max_water:
                max_water = water
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_water
