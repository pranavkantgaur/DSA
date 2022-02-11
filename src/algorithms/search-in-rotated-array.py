'''
1. Check if the array is rotated:
   1.1. if not, do binary search for input element: if arr[0] < arr[n - 1]: not rotated, else, rotated around arr[0] as pivot : O(logn)
   1.2. if it is:
        1.2.1 Either, unrotate it and do binary search, or: # unrotating may not be O(logn)
              1. Do binary search over rotated array(Note: pivot is known, arr[0])
        1.2.1.a Using quick-partition: O(n)
              1. Since arr[0] is the pivot, the input array is sorted on both sides of pivot(when pivot is at its correct position)
                 1.1. Get correct location of pivot, say ith index: (O(n))
                 1.2. Do binary search over left and right sub-arrays(both are sorted) : O(logn)
        1.2.1.b Binary search on rotayted array with local surface check:
              
                  .   
                .       .           
              .       .         .      .
                         .          .
               (a)     (b)        (c)      
               View at the swtiching point(meeting point of (sorted) end of array and start of (sorted) array in rotated form)
               
              
              1. Visit mid of array: check the surface, if it is increasing, then continuie binary search logic
              2. if the surface has a dip: arr[i  -1] < arr [i ] > arr[i + 1]
                 2.1. I know that max value of increasing part is arr[i  - 1] and min value of de[]
Desired TC: O(logn)              
        
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        low = 0, high = len(nums) -  1 
        while(low < high):
            mid = low + (high - low) // 2
            if target == nums[mid]: 
                return mid
            if nums[mid] > nums[mid + 1]: #so a[mid + 1] is the smallest element of the array and a[mid] is the largest element of the array: 
                if target > nums[mid]: # larger than largest
                    return -1
                if target < nums[mid + 1]: # smaller than smallest
                    return -1
                else:
                    if target > nums[low]: 
                        high = mid - 1
                    if target < nums[low]: 
                        low = mid + 1
            if nums[mid] < nums[mid + 1]: #this is expected of a sorted array, continue with conventional binary search process:
                if target > nums[mid]: 
                    low = mid + 1
                else: 
                    high = mid - 1
        return -1        
        
