'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
BF: 
0. Check if arr[0] <= target <= arr[n - 1]: if true then continue else return [-1, -1]
1. Linearly search for the element from left to right
2. Mark the first position where the element is found
3. Continue untill current element is different from target value, set last index as current - 1
4. return start, last index

TC: O(n)
SC: O(1)

Binary search:
0. Check if arr[0] <= target <= arr[n - 1]: if true then continue else return [-1, -1]
1. Locate the element in the array, say index i = bsearch(low, high, target)
2. Check if a[i - 1] == target, if true: bsearch(low, i - 1, target) 
3. Check if a[i + 1] == target, if true: bsearch(i + 1, high, target)
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
