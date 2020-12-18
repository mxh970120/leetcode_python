'''
Author: mxh970120
Date: 2020.12.18
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        for c in t:
            if c not in letters:
                return c
            letters[c] -= 1
            if letters[c] < 0:
                return c



if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    solu = Solution()
    print(solu.findTheDifference(s, t))