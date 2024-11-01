from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find maximum profit from buying and selling stock once.
        
        Args:
            prices: List of stock prices where prices[i] is price on day i
            
        Returns:
            Maximum profit possible (0 if no profit possible)
        """
        # Handle edge cases
        if len(prices) <= 1:
            return 0
            
        min_price = 10001  # Arbitrary large number
        max_profit = 0  # Track maximum profit possible
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
