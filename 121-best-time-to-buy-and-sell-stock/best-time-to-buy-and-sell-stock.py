class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float("inf")
        max_profit=0
        for i in range(len(prices)):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit



        # Brute force Approach(199 test case pass)
        # # profit=0
        # max_profit=0
        # n=len(prices)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #     #     s=prices[j]-prices[i]
        #     #     if(profit<s):
        #     #         profit=s
        #     # if(profit>max_profit):
        #     #     profit,max_profit=0,profit
        #         if(prices[i]<prices[j]):
        #             p=prices[j]-prices[i]
        #             max_profit=max(p,max_profit)

        # return max_profit
