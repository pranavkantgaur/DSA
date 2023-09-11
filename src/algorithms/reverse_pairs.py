'''
# https://leetcode.com/problems/reverse-pairs/
1. [1,1,1,1], o/p -> 0 
2. [1,4, 1, 3 , 1] -> 3 
3. [1,2,3,4,5] -> o/p - > 0
4. [4,3,2,1] -> 6
5. [4, -5, 0] -> 2


Naive algorithm: TC-> O(n^2), SC -> O(1)
1. For each number, check if there is a index in remaining array where reverse-pair condition is satisfied?

count = 0
for i, first_num in enum(nums):
  for j, second_num in  enum(i +1, nums):
  if nums[second_num] * 2 < first_num:
  	count += 1
return count  	

Bottlenecks:
1. Possible to have TC: O(n), SC: O(1) ?
2. Whether merge sort type approach will help in reducing the TC?
   1. For problem os size 2, solution is based on nums[0] > 2*nums[1], return 1, else return 0
   2. result(n) = result(0, n / 2) + result(n/2, n - 1)    + merge(0, n-1) # count number of reverse pairs generated due merging of (0, n/2) and (n/2 , n-1) arrays.
'''
