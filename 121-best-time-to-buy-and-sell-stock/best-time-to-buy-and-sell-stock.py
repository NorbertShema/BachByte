class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Understand
            Input: list(array of price)
            Output: Int (the max profit after buying and selling)
            Constraints: Time moves in one direction, cant sell before you buying.
            Edge cases: empty array. Return 0

        Plan:
            -Set the max_profit = 0 :for easy tracking
            -Set min_price = inf : Because we dont know the min_price and we replace it when we find something smaller till we get to the min.
            -Now we need to compute max profit

        Implement:

        """
        max_profit =0
        min_price =float ('inf')
        
        for price in prices:
            if price < min_price:
                min_price = price #check if the current price is smaller to update the min_pric

            profit = price - min_price #get the current profit

            if profit > max_profit:
                max_profit = profit  #get the max_profit

    
        return max_profit


    #Time: O(n)                
    #Space: O(1)
