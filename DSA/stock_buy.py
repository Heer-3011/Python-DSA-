class Solution:
    def maxProfit(self, prices):
        #print(prices)
        m=0
        for i in range(0,len(prices)+1):
            for j in range(i+1,len(prices) ):
                m=max(m,(prices[j]-prices[i])) 
        return m
s1=Solution()
print(s1.maxProfit([7, 10, 1, 3, 6, 9, 2]))
print(s1.maxProfit([7, 6, 4, 3, 1]))
print(s1.maxProfit([1, 3, 6, 9, 11]))