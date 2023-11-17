# https://leetcode.com/problems/online-stock-span/
# get the index of next greater element towards the left side in O(1), build a mono. decreasing stack using prices, store the next greater for each id in a hashmap, push to the stack if value is smaller than top else pop elements
# return return 1 + current id  - top_element_value(an id), push current id to top of stack
class StockSpanner():
	def __init__(self):
		self.stack = []
		self.current_id = 0

	def next(self, price):
		while(len(self.stack) and price >= self.stack[-1][0]):
			self.stack.pop()
		if len(self.stack) == 0:
			stock_span = self.current_id + 1	
		else:
			stock_span = self.current_id - self.stack[-1][1]
		self.stack.append([price, self.current_id])
		self.current_id += 1
		return stock_span      


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
