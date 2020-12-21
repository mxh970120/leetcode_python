'''
Author: mxh970120
Date: 2020.12.21
'''

class Solution:
    def minCostClimbingStairs(self, cost) :
        # 动态规划
        n = len(cost)
        dp = [0] * (n + 1)  # 这里的dp[0]和[1]均为0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]



if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solu = Solution()
    print(solu.minCostClimbingStairs(cost))