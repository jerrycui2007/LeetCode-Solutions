from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit from multiple buy-sell transactions.
        
        Args:
            prices: List of stock prices where prices[i] is price on day i
            
        Returns:
            Maximum profit possible from multiple transactions
        """
        # Handle edge cases
        if len(prices) <= 1:
            return 0
            
        total_profit = 0
        
        # Add up all positive price differences
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit


if __name__ == "__main__":
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
