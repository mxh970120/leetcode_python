'''
Author: mxh970120
Date: 2020.12.17
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 偷懒的方法
        # return len(s.strip().split(' ')[-1])

        length = len(s)
        num = 0
        for i in range(length - 1, -1, -1):
            if s[i] == " ":
                if num == 0:
                    continue
                else:
                    break
            else:
                num += 1
        return num


if __name__ == '__main__':
    prices = "Hello World"
    solu = Solution()
    print(solu.lengthOfLastWord(prices))