# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal.append([1])
        for each row from 1 to numRows:
	        current_row = []
	        current_row.append(1)
	        start = 0
	        end = 1
	        while(end <= row - 1) # i is the row id of previous row	
		        current_row.append(pascal[row - 1][start] + pascal[row - 1][end])
		        start += 1
		        end += 1
	        current_row.append(1)		
	        pascal.append(current_row)
    return pascal		
