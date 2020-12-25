'''
Author: mxh970120
Date: 2020.12.13
'''

class Solution:
    def generate(self, numRows):
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret




if __name__ == '__main__':
    s = 5
    solu = Solution()
    print(solu.generate(s))