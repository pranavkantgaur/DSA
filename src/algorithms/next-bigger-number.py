# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
'''
Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"

Approach:
1. Vist from right letter to left letter
   1.1. If a[i - 1] > a[i]: continue
   1.2. else: search k such that i+1 <= k <= n - 1 and 
        a[k] > a[i - 1] and a[k] < a[j] where i + 1 <= j <= n - 1
        swap a[k], a[i - 1]
        sort a[i:n - 1]       
        return a
   1.3. return False        
'''
#User function Template for python3

class Solution:
    def getNextLargerNumber(self, value, start_id, end_id, arr): # 4, 3, 5, arr : [9, 7, 6]
        # input is a sorted array(decreasing)
        # locate a number just greater than the input number in the array
        while(start_id < end_id):
            mid_id = start_id + (end_id  - start_id) // 2
            if arr[mid_id] > value:
                start_id = mid_id + 1
            else: # equality is not possible for this input
                end_id = mid_id - 1
        # check if arr[start_id] is > than value? means start_id == end_id, always?
        if arr[start_id] < value:
            return mid_id
        else:    
            return start_id
         
    def nextPermutation(self, N, arr):
        # code here
        #for (i = n - 1; i <= 0; i--):
        for i in range(N - 1, -1, -1):
            if arr[i - 1] > arr[i]:
                continue
            else:
                k = self.getNextLargerNumber(arr[i -  1], i, N - 1, arr)
                t = arr[k]
                arr[k] = arr[i - 1]
                arr[i - 1] = t
                arr[i:] = sorted(arr[i:])
                return arr
        return None            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends

'''
TC: O(n)
SC:
'''
   
