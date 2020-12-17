'''
Author: mxh970120
Date: 2020.12.17
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # python偷懒
        # return bin(int(a, 2) + int(b, 2))[2:]

        res = ''
        i = len(a)-1
        j = len(b)-1
        carry = 0
        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            res = str(carry % 2) + res
            i, j, carry = i - 1, j - 1, carry//2

        return res



if __name__ == '__main__':
    a = "1010"
    b = "1011"
    solu = Solution()
    print(solu.addBinary(a, b))