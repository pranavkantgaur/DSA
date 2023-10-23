# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# greedy approach gives o(n), just keep transacting if the next selling price will be higher than current price.

class Solution {
public:
    int stockBuyAndSell(int n, int price[]) {
        int profit = 0;
        for (int i = 1; i < n; i++) {
            if (price[i] > price[i - 1])
                profit += price[i] - price[i - 1];
        }
        return profit;
    }
};
