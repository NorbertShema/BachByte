class Solution(object):
    def maxProfit(self, prices):
        """
        : type prices: List[int]
        :rtype: int

        Understand:
            - Input: List of stock prices (prices[i] = price on day i)
            - Output: Int (the maximum profit from one buy/sell transaction)
            - Constraints:
                - Must buy before selling (time moves forward only)
                - At most one transaction (one buy + one sell)
            - Edge cases:
                - Empty array → return 0
                - Single price → return 0 (can’t sell)

        Plan:
            - Initialize max_profit = 0 (no profit yet)
            - Initialize min_price = ∞ (start high, will update when a smaller value is seen)
            - For each price in the list:
                - Update min_price if we find a smaller price
                - Calculate profit = current price - min_price
                - Update max_profit if profit is greater
            - Return max_profit

        Implement:
        """
        max_profit = 0
        min_price = float('inf')  # smallest price seen so far
        
        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price

            # Calculate profit if sold today
            profit = price - min_price

            # Update max_profit if this profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit

    # Time Complexity: O(n) → single pass through prices
    # Space Complexity: O(1) → only a few variables stored
