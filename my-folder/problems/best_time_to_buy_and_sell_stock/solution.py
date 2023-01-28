class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruteforce
        # maxProfit = float('-inf')
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        
        # return maxProfit if maxProfit > 0 else 0


        # one_pass
        # minPrice = float('inf')
        # maxProfit = float('-inf')
        # for i in range(len(prices)):
        #     if prices[i] < minPrice:
        #         minPrice = prices[i]
            
        #     elif prices[i] - minPrice > maxProfit:
        #         maxProfit = prices[i] - minPrice

        # return maxProfit if maxProfit > 0 else 0


        #   public int maxProfit(int[] prices) {
        # int[] dp = new int[prices.length];
        # dp[0] = 0;
        # int min = prices[0];
        # for (int i = 1; i < prices.length; i++) {
        #     min = Math.min( min, prices[i]);
        #     dp[i] = Math.max( dp[i-1],  prices[i] - min );
        # }
        # return dp[prices.length - 1];


        dp = [0] * len(prices)
        minVal = float('inf')
        for i in range(len(prices)):
            minVal = min(minVal, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minVal)
        return dp[-1]
