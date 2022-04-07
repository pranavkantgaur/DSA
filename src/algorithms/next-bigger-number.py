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
    def getNextLargerNumber(self, value, start_id, end_id, arr):
        # locate with bsearch
        #rightSubArr = arr[start_id:end_id]
        # search for value in rightSubArr
        while(start_id < end_id):
            mid_id = start_id + (end_id  - start_id) // 2
            if arr[start_id + mid_id] > value:
                start_id = start_id + mid_id + 1
            else:
                end_id = start_id + mid_id - 1
        # check if arr[start_id] is > than value?           
      
    def nextPermutation(self, N, arr):
        # code here
        for (i = n - 1; i <= 0; i--):
            if arr[i - 1] > a[i]:
                continue
            else:
                k = self.getNextLargerNumber(arr[i -  1], i, n - 1, arr)
                t = a[k]
                a[k] = a[i - 1]
                a[i - 1] = t
                arr[i:].sort()
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
   
