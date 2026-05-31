"""LeetCode 121: Best Time to Buy and Sell Stock.

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Track the lowest price seen before each possible sale.

        Time: O(n)
        Space: O(1)
        """
        lowest_price = float("inf")
        best_profit = 0
        for price in prices:
            lowest_price = min(lowest_price, price)
            best_profit = max(best_profit, price - lowest_price)
        return best_profit
