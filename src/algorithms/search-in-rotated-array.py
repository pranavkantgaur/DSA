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
    
    
    
    def bSearch(self, low, high, target):
        if low <= high:
            mid = low + (high - low) // 2
            if a[mid] == target:
                return mid
            if a[mid] > target:
                bSearch(low, mid - 1, target)
            if a[mid] < target:
                bsearch(mid + 1, high, target)
        else:
            return -1
    
    
    def search(self, nums: List[int], target: int) -> int:        
        #check if array is rotated
        if nums[0] < nums[len(nums) - 1]:
            return self.bsearch(0, len(nums) - 1, target)
        #if not, array is rotated
        else:
            low = 0
            high = len(nums) - 1
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            # check for transition point
            if nums[mid] > nums[mid - 1] and nums[mid + 1] < nums[mid]:
                #check a[low] and a[mid - 1] wrt. target:
                if a[mid - 1] == target:
                    return mid - 1
                if a[low] == target:
                    return low
                if a[low] < target and a[mid - 1] > target:
                    return self.bsearch(low, mid - 1, target)
                #check a[mid + 1] and a[high] wrt. target                
                if a[mid + 1] == target:
                    return mid + 1
                if a[high] == target:
                    retun high
                if a[mid + 1] < target and a[high] > target:
                    return self.bsearch(target, mid + 1, high)
                else:
                    return -1 # target is neither in left half nor in right half
            else: # not a transition point
                if a[mid] > target:
                    return self.bsearch(low, mid - 1, target)
                else:
                    return self.bsearch(mid + 1, high, target)
        
        
   
        
