'''
Author: mxh970120
Date: 2020.12.16
'''

class Solution:
    def countAndSay(self, n) -> str:
        # 使用指针start，end和长度length，读取到第一段之后，更新start，再变化end，得到length
        res = "1"
        if n == 1: return res

        for i in range(n - 1):
            start = res[0]
            length = 1
            ans = ""
            for j in range(1, len(res)):
                end = res[j]
                # start不等于end，即第一段停止了
                if start != end:
                    ans = ans + str(length) + str(start)
                    start = end  # 更新start
                    length = 0  # 重置length
                length += 1
            res = ans + str(length) + str(start)  # 更新 n=i时的res
        return res


if __name__ == '__main__':
    n = 5
    solu = Solution()
    print(solu.countAndSay(n))