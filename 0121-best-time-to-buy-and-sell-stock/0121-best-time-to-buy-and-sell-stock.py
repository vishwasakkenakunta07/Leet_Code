class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = 0
        bp = prices[0]
        for i in prices:
            cp = i
            if(i<bp):
                bp = i
            maxi = max(maxi,cp-bp)
        return maxi
        
        
        


        