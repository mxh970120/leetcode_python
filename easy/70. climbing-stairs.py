'''
Author: mxh970120
Date: 2020.12.18
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划
        dp = [0] * (n + 1)
        dp[0] = 1  # 第0级到第0级只有一种可能，理解不了可以用dp[2]反推
        dp[1] = 1  # 第0级到第1级也只有一种可能
        for i in range(2, n + 1):
            # 因为每次只能爬 1 级或 2 级，所以数量为二者之和
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]





if __name__ == '__main__':
    s = 4
    solu = Solution()
    print(solu.climbStairs(s))