'''
Author: mxh970120
Date: 2020.12.16
'''

class Solution:
    def maxSubArray(self, nums) -> int:
        # 暴力解法 超时了QAQ
        # res = float("-inf")
        # length = len(nums)
        #
        # for i in range(0, length):
        #     sum = 0
        #     for j in range(i, length):
        #         sum += nums[j]
        #         if sum > res:
        #             res = sum
        # return res

        # 动态规划
        length = len(nums)
        dp = [0]*length
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, length):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solu = Solution()
    print(solu.maxSubArray(nums))