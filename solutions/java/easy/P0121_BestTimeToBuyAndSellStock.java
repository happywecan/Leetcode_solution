/**
 * LeetCode 121: Best Time to Buy and Sell Stock.
 *
 * Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 */
public class P0121_BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        for (int i = 1;i < prices.length;i++){
            int profit = prices[i] - minPrice;
            if (profit > maxProfit) {
                maxProfit = profit;
            }
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        P0121_BestTimeToBuyAndSellStock solution = new P0121_BestTimeToBuyAndSellStock();
        System.out.println(solution.maxProfit(new int[] {7, 1, 5, 3, 6, 4})); // Expected: 5
        System.out.println(solution.maxProfit(new int[] {7, 6, 4, 3, 1}));    // Expected: 0
    }
}
