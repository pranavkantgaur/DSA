'''
Google docs:

We are given a row-wise sorted matrix of size r*c, we need to find the median of the matrix given. It is assumed that r*c is always odd.

Examples: 

Input: 1 3 5
        2 6 9
        3 6 9
Output: Median is 5
If we put all the values in a sorted 
array A[] = 1 2 3 3 5 6 6 9 9)
Input: 1 3 4
       2 5 6
       7 8 9
Output: Median is 5

TC: O(rc log(rc))

Find the rc/2th largest element?

Lets say I have rc medians for sorted subsequnces? How to get median of entire sorted number list?

How many numbers to visit before being sure about the median element?




def get_median_sorted_matrix(nums):
	nums_list = [num for i in ranage(len(nums)) for j in range(len(nums[0])) num = nums[i][j]]
	nums = sorted(nums)
	r = len(nums)
	c = len(nums[0])
	return nums[rc/2]
	

Approach2:
1. Take last element of first row, e1
2. b search it in all remaining rows
3. count number of elements on the left side of e1
4. if count > rc / 2 then median is on left side of e1, if count = rc/2 then e1 is the median, if count < rc/2 then median is on right side of e1

Approach 2 rephrased:
1. For each element, binary search that element in rest of the rows
2. Add the elements on left side for each row
3. if number of element on left side > rc / 2 -> median is on left side, else if < rc / 2 median is on right side.


1 2 3 5 6 9




Approach 3: Cyclic sort
1. Get min and max numbers in the matrix
2. We have rc numbers in range [min, max], sort these numbers using cyclic sort in O(rc) TC and O(rc) SC
3. Return the median

def get_median_sorted_matrix(nums):
   min = min([num for i in range(len(nums) num = nums[i][0])])
   max = max([num for i in range(len(nums) num = nums[i][-1])])
   arr = []
   while(min <= max):
   	mid = (max + min) / 2
	count_nums_less = 0
   	for row in nums:
   		count_nums_less += get_count(mid, row) # get number of elements in the row less than 'mid'
	if count_nums_less < rc / 2:
		min = mid + 1
	if count_nums_less > rc / 2:
		max = mid - 1
	else:
		return mid				   		
   		

Input: 1 3 4
       2 5 6
       7 8 9
Output: Median is 5   

1-9, mid = 5, need 4 numbers less than mid
   





==================================

'''
