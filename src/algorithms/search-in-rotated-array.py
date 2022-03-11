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
    class Solution: 
        def bSearch(self, low, high, target, nums):
        if low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                #print("Match at: ", nums[mid], target, low, mid, high)
                return mid
            if nums[mid] > target:
                return self.bSearch(low, mid - 1, target, nums)
            if nums[mid] < target:
                return self.bSearch(mid + 1, high, target, nums)
        else:
            return -1
    
    
    def search(self, nums: List[int], target: int) -> int:        
        #check if array is rotated
        if nums[0] < nums[len(nums) - 1]:
            return self.bSearch(0, len(nums) - 1, target, nums)
        #if not, array is rotated
        else:
            low = 0
            high = len(nums) - 1
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            # check for transition point
            #print("MID:", mid, low, high)
            if mid - 1 >= 0 and mid + 1 <= len(nums) - 1:
                if nums[mid] > nums[mid - 1] and nums[mid + 1] < nums[mid]:
                    #check a[low] and a[mid - 1] wrt. target:
                    if nums[mid - 1] == target:
                        return mid - 1
                    if nums[low] == target:
                        return low
                    if nums[low] < target and nums[mid - 1] > target:
                        return self.bSearch(low, mid - 1, target, nums)
                    #check a[mid + 1] and a[high] wrt. target                
                    if nums[mid + 1] == target:
                        return mid + 1
                    if nums[high] == target:
                        return high
                    if nums[mid + 1] < target and nums[high] > target:
                        return self.bSearch(mid + 1, high, target, nums)
                    else:
                        return -1 # target is neither in left half nor in right half
                elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    if target == nums[low]:
                        return low
                    if target == nums[mid  -1]:
                        return mid - 1
                    if target > nums[low] and target < nums[mid - 1]:
                        return self.bSearch(low, mid - 1, target, nums)
                    if target == nums[mid + 1]:
                        return mid + 1
                    if target == nums[high]:
                        return high                        
                    if target > nums[mid + 1] and target < nums[high]:
                        return self.bSearch(mid + 1, high, target, nums)
                    else:
                        return -1
                else: # not a transition point
                    # we can still run binary search on sorted part and 'modified' bsearch in the part with transition point
                    # check for transition point in subparts on left and right of current 'mid'
                    if nums[low] > nums[mid - 1]: # contains transition point
                        if target >= nums[mid + 1] and target <= nums[high]:
                            return self.bSearch(mid + 1, high, target, nums)
                        else:
                            return_val = self.search(nums[low: mid], target)
                            if return_val != -1:
                                return low + return_val
                            else:
                                return -1
                    elif nums[mid + 1] > nums[high]: # contains transition point
                        if target >= nums[low] and target <= nums[mid - 1]:
                            return self.bSearch(low, mid - 1, target, nums)
                        else:
                            #print("check: ", nums[mid + 1: high + 1])
                            return_val =  self.search(nums[mid + 1: high + 1], target)
                            if return_val != -1:
                                return mid + 1 + return_val 
                            else:
                                return -1
                    else:
                        return None # logically not possible
            else:
                #print("out of bound with array length:", len(nums))
                if mid - 1 < 0:
                    #print("HERE")
                    if mid + 1 <= len(nums) - 1:
                        if nums[mid + 1] == target:
                            return mid + 1
                        else:
                            #print("TES")
                            return -1
                    else:
                        return -1
                else:
                  pass  
        
