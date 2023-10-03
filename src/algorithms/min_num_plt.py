# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def bsearch(self, num, arr):
        low = 0
        high = len(arr) -1
        while(low < high):
            mid = low + (high - low) // 2 #(high - low) // 2
            if arr[mid] > num: # left
                high = mid - 1
            if arr[mid] < num: # right
                low = mid + 1
            else:
                return mid
        return low                
        
    def minimumPlatform(self,n,arr,dep):
        # code here
        max_plt = 0
        for i, dept_time in enumerate(dep):
            j = self.bsearch(dept_time, arr[i+1:])
            n_plt = j + 1
            #print('J: ', j)
            if n_plt > max_plt:
                max_plt = n_plt
        return max_plt
