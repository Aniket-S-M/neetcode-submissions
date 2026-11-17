class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        csum = 0
        wsum = 0 
        p = 0
        j = 1
        r = 1 
        l  = 0   

        while r < len(prices):
            if prices[r] > prices[l] : 
                csum = prices[r] - prices[l]
                p = max(p,csum)
            else : 
                l = r 
            
            r += 1  
            
                
        return p 

                
        