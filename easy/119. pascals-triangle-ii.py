'''
Author: mxh970120
Date: 2020.12.13
'''

class Solution:
    def getRow(self, rowIndex):
        # 初始化一个列表；
        # 遍历列表，从第一行开始填充，直到rowIndex，注意初始的为第0行；
        # 插入0在该行的最前面；
        # 遍历这一行的数据，将第一个数据与第二个相加，得到第一个的新数据。

        res = [1]
        for i in range(rowIndex):
            res.insert(0, 0)
            for j in range(len(res)-1):
                res[j] = res[j] + res[j+1]
        return res

if __name__ == '__main__':
    s = 5
    solu = Solution()
    print(solu.getRow(s))