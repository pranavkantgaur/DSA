# https://practice.geeksforgeeks.org/problems/number-of-coins
#User function Template for python3
class Solution:
	def minCoins(self, coins, M, V):
		# code here
		'''
		1. Pick a coin if v <= V: 1 + update coins, V and call again -> A
		2. Dont pick if v > V: update coins and call again -> B
		3. return min(A, B)
		
		
		greedy:
		1. For each coin, check if its feasible to form change, if not move to next coin
		2. If possible, then , update 
		'''
		if len(coins) == 0: return -1
		if V < min(coins): return -1
		# include
		if V >= coins[0]:
		    include = 1 + self.minCoins(coins, M, V - coins[0])
		    exclude = self.minCoins(coins[1:], M - 1, V)
		    result = min(include, exclude)
		    # exclude
		else:
		    exclude = self.minCoins(coins[1:], M - 1, V)
		    result = exclude
		# return
		return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends
