'''
Author: mxh970120
Date: 2020.12.17
'''

class Solution:
    def maxProfit(self, prices, fee):
        # 动态规划
        dp = [0]*2
        # 对于第0天：
        # 不持有： dp[0] = 0
        # 持有（即花了 price[0]price[0] 的钱买入）： dp[1] = -prices[0]
        dp[0] = 0  # 今天不持有可获得的最大利润
        dp[1] = -prices[0]  # 今天持有可获得的最大利润
        for i in range(1, len(prices)):
            dp[0] = max(dp[0], dp[1] + prices[i] - fee)
            dp[1] = max(dp[1], dp[0] - prices[i])
        return dp[0]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    solu = Solution()
    print(solu.maxProfit(prices, fee))