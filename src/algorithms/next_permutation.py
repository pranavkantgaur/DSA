# https://leetcode.com/problems/next-permutation/

* When you sort the subarray you get the lowest possible order for that subarray: 
* For one MSB, we can generate first permution as sort(remaining numbers), then next perm. is 

[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2]

* Flip the last 2 numbers, then the permustions for last 2 numbers are over.
* Then select the next largest element in the array and put it on the 

* For any MSB number, sorted subarray forms the first permutation. 
* And recursively, reach to the last 3 numbers where for the MSB which is the 3rd largest number of array, flipping last 2 numbers forms the next permutation



if n == 3: # base condition
  next_per(n-3, ... n-1) = num[n - 3] + num[n-1] + num[n - 2]	# flip

if num is not the max order for num[0] as MSB:
	next_per(0...n-1) = num[0] + next_per(1...n-1)
else:
	next_highest_num = get_index(num, sorted(0, n - 1)) + 1 # next highest number's index
	t = num[0]
	num[0] = next_highest_num
	next_per(0, n - 1) = num[0] + sorted(1, n - 1)


# recursion:
1. Sort the array
2. For each MSB: generate all permutations in the order (recursive call)	
3. The base case is when the array has length 3: In that case, flipping last two numbers is the max order permutation(lowest order being the sorted 2 number array)
4. Once base case is reached, return

# for a given array: check last 2 digits if nums[n-1] < nums[n - 2] (means max order for last 3 already present.), 
then change the MSB as the next highest number and continue recursion.


I think the problem asked is much simpler than generating all order permutations, as it asks for the next permutation only:
