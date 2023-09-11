'''
# https://leetcode.com/problems/4sum/
Clarify:
1. Problem with no solution, what to return?
2. Duplicaton allowed?
3. Return answrr in any order? index of elements in a quadreplet need not be sorted? 

Test-cases"
1. [1, 2, 3, 4, 5], t = 7, O/P->    None
2. [1,2,2, 4, 5,5, 2,3], t = 7, o/p=[1, 2,2,2]
3. [10^8, 1, 0, 1], t = 2, o/p = None # may explore buffer overflow?
4. [-10^8, -10^8, 1, 1], t = 2, o/p = None # underflow check?
5. ??



Naive algo: TC: O(n^4), SC: O(1)
1. For each quadraplet, evaluate its sum and check if it is equal to target, if so append to the result array.

for id1, num1 in enum(nums)
  for id2, num2 in enum(nums[id1+ 1:])
    for id3, num3 in enum(nums[id2 + 1: ])
      for id4, num4 in enum(nums[id3 + 1: ]):
      	if num1 + num2 + num3 + num4 == target:
      	  result.append([num1, num2, num3, num4])	

      	  
Composite algo:
1. To solve using solutions for 3, 2,1sum problems conditioned over target - num for each num?
    1. for nums = [1,0,-1,0,-2,2], target = 0, -> 3-sum over ([0,-1,0,-2,2], target = -1) -> 2-sum over [-1,0,-2,2], target=-1 -> 1 sum over [0, -2, 2], target = 0



def 3sum(num, target = t):
	for idx, num in enum(nums)
		if 2sum(nums[:idx] + nums[idx + 1:], target = -1.0 * (target + num)):
		  return result = 
target = k
for id, num in enum(nums):
  3sum(nums[:id], nums[id+1:], target = )
'''
