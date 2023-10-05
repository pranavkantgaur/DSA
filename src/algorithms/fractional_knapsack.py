#User function Template for python3
# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # code here
        '''
        1. Sort arr, w based on max value per weight in descending order
        2. For each item, if adding it feasible, add item's value to total value and its weight, else add maximum possible fraction of it
        3. return total value
        '''
        #value_sort = sorted(value)        
        index_array = [(i, arr[i].value / arr[i].weight) for i in range(len(arr))]
        #print('index: ', index_array)
        index_array.sort(reverse = True, key = lambda a:a[1])
        #print('index sorted: ', index_array)
        

        value = 0.0
        curr_w = 0.0
        for id in range(len(index_array)):
            #if curr_w + sorted_weight[id]
            av_quota = W - curr_w
            if av_quota == 0:
                break
            if arr[index_array[id][0]].weight <= av_quota:
                value += arr[index_array[id][0]].value
                curr_w += arr[index_array[id][0]].weight
            else:
                value += (av_quota / arr[index_array[id][0]].weight)* arr[index_array[id][0]].value
                curr_w += av_quota
                
        return value

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends
