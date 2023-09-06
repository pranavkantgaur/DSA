# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



Naive algorithm: TC -> O(n^2), SC->T(1)
1. For each pair, 
   * Compute profit of transaction
   * Update max profit so far
2. Return max profit so far   

Possible to reduce it to say TC->O(nlogn)?
* We cannot sort the array
* What are the bottleneck?
  * Enumerating all possible pairs? There may be some which need not be explored?
  
* Can 2-pointer approach help?  
  * Progressively iterate on start, end values which are smaller, greater respectively than previous selections.
     start = 0
     end = len(array) - 1
     while(start < end):
       profit = val[end] - val[start]
       if max_profit < profit:
       	max_profit = profit
       cand_start = start
       cand_end = end	
       while(val[cand_start] >= val[start] and cand_start < end):	
          cand_start += 1
       profit = val[end] - val[cand_start]
       if max_profit < profit:
       	max_profit = profit          
       while(val[cand_end] <= val[end] and cand_end > start):	
          cand_end -= 1
       profit = val[cand_end] - val[start]
       if max_profit < profit:
       	max_profit = profit          

	start = cand_start
	end = cand_end

     return max_profit	
   
   * Why this algorithm is correct? 	          
     * It passes the above 2 test-cases
     * Are there test-cases where it fails? 
       * prices = [7,7,,7,7,7,7,7] -> OP = 0 - Passes
       * [1, 2, 3, 4, 6], O = 5, Passes
       * Seems like it will catch the optimal pair,
'''
